"""Database conversion utility for HyperCode research data.

This module provides functionality to convert research database files into
HyperCode's standard database format with proper validation and error handling.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("conversion.log")],
)
logger = logging.getLogger(__name__)


class DatabaseConversionError(Exception):
    """Custom exception for database conversion errors."""

    pass


def validate_input_file(file_path: Union[str, Path]) -> None:
    """Validate the input file exists and is accessible.

    Args:
        file_path: Path to the input file.

    Raises:
        DatabaseConversionError: If file validation fails.
    """
    path = Path(file_path)
    if not path.exists():
        raise DatabaseConversionError(f"Input file not found: {file_path}")
    if not path.is_file():
        raise DatabaseConversionError(f"Input path is not a file: {file_path}")
    if path.stat().st_size == 0:
        raise DatabaseConversionError(f"Input file is empty: {file_path}")


def load_research_data(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Load and validate research data from JSON file.

    Args:
        file_path: Path to the research database JSON file.

    Returns:
        Parsed research data as a dictionary.

    Raises:
        DatabaseConversionError: If loading or parsing fails.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as e:
                raise DatabaseConversionError(
                    f"Failed to parse JSON in {file_path}: {str(e)}"
                )
    except IOError as e:
        raise DatabaseConversionError(f"Failed to read file {file_path}: {str(e)}")


def convert_research_db(
    input_path: Union[str, Path],
    output_path: Optional[Union[str, Path]] = None,
    entity_type: str = "research",
    overwrite: bool = False,
) -> Path:
    """Convert research database to HyperCode format.

    Args:
        input_path: Path to the input research database file.
        output_path: Path where to save the converted database. If None, will
            use the input path with '-converted' suffix.
        entity_type: Type to assign to the converted entities.
        overwrite: Whether to overwrite existing output file.

    Returns:
        Path to the converted database file.

    Raises:
        DatabaseConversionError: If conversion fails.
    """
    start_time = datetime.now()
    logger.info(f"Starting database conversion for {input_path}")

    # Validate input file
    try:
        validate_input_file(input_path)
    except DatabaseConversionError as e:
        logger.error(f"Input validation failed: {e}")
        raise

    # Set default output path if not provided
    input_path = Path(input_path)
    if output_path is None:
        output_path = input_path.with_stem(f"{input_path.stem}-converted")
    output_path = Path(output_path)

    # Check if output file exists and handle accordingly
    if output_path.exists() and not overwrite:
        raise DatabaseConversionError(
            f"Output file {output_path} already exists. Use overwrite=True to replace."
        )

    # Load and validate research data
    try:
        research_db = load_research_data(input_path)
        logger.info(f"Successfully loaded research data from {input_path}")
    except DatabaseConversionError as e:
        logger.error(f"Failed to load research data: {e}")
        raise

    # Create a new database with the expected format
    converted_db = {
        "metadata": {
            **research_db.get("metadata", {}),
            "conversion": {
                "original_file": str(input_path),
                "conversion_time": datetime.utcnow().isoformat(),
                "tool": "convert_research_db",
            },
        },
        "entities": [
            # Convert the research data into entities
            {
                "id": f"{entity_type}_metadata_{i}",
                "type": entity_type,
                "content": entity_data,
                "file": str(input_path),
                "line": 0,
                "docstring": "Research database converted to entity format",
            }
            for i, entity_data in enumerate(
                research_db.get("entities", [research_db]), 1
            )
        ],
    }

    # Save the converted database
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(converted_db, f, indent=2, ensure_ascii=False)

        # Verify the output file was created and is valid
        if not output_path.exists() or output_path.stat().st_size == 0:
            raise DatabaseConversionError(
                "Failed to create output file or file is empty"
            )

        # Verify the output is valid JSON
        with open(output_path, "r", encoding="utf-8") as f:
            json.load(f)  # Will raise JSONDecodeError if invalid

        duration = (datetime.now() - start_time).total_seconds()
        logger.info(
            f"Successfully converted database in {duration:.2f} seconds. "
            f"Output: {output_path}"
        )
        return output_path

    except (IOError, json.JSONDecodeError) as e:
        error_msg = f"Failed to save converted database to {output_path}: {str(e)}"
        logger.error(error_msg)
        # Clean up potentially corrupted output file
        if output_path.exists():
            try:
                output_path.unlink()
            except OSError:
                pass  # If we can't delete it, just move on
        raise DatabaseConversionError(error_msg) from e


def main():
    """Command-line interface for the database conversion tool."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert research database to HyperCode format."
    )
    parser.add_argument(
        "input", type=str, help="Path to the input research database file"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to save the converted database (default: <input>-converted.json)",
    )
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        default="research",
        help="Entity type for the converted data (default: research)",
    )
    parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite output file if it exists"
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()

    # Configure logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    try:
        convert_research_db(
            input_path=args.input,
            output_path=args.output,
            entity_type=args.type,
            overwrite=args.overwrite,
        )
    except DatabaseConversionError as e:
        logger.error(f"Conversion failed: {e}")
        return 1
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
