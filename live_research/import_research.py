#!/usr/bin/env python3
"""
Script to import all JSON research files into the database.
"""

import json
import logging
from pathlib import Path
from .database import setup_database

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def import_research_data():
    """Import all JSON research files into the database."""
    # Initialize database
    db = setup_database()

    # Path to the research data JSON directory
    data_dir = Path("c:\\Users\\lyndz\\Downloads\\hypercode PROJECT\\hypercode\\data")
    json_dir = data_dir / "reseach data json"

    if not json_dir.exists() or not json_dir.is_dir():
        logger.error(f"Research data directory not found: {json_dir}")
        return

    # Find all JSON files
    json_files = list(json_dir.glob("*.json"))
    if not json_files:
        logger.warning(f"No JSON files found in {json_dir}")
        return

    logger.info(f"Found {len(json_files)} JSON files to process...")

    total_imported = 0

    # Process each JSON file
    for json_file in json_files:
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                entry = json.load(f)

            # Add entry to database
            if db.add_research_entry(entry):
                total_imported += 1
                logger.debug(f"Imported: {json_file.name}")
            else:
                logger.warning(f"Failed to import: {json_file.name}")

        except json.JSONDecodeError as e:
            logger.error(f"Error parsing {json_file.name}: {e}")
        except Exception as e:
            logger.error(f"Error processing {json_file.name}: {e}")

    logger.info(
        f"Import complete. Successfully imported {total_imported}/{len(json_files)} entries."
    )


if __name__ == "__main__":
    import_research_data()
