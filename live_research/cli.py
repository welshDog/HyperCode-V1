import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any
from datetime import datetime
from .database import setup_database


def print_entry(entry: Dict[str, Any], detailed: bool = False):
    """Print a research entry in a readable format."""
    print("\n" + "=" * 80)
    print(f"ID:      {entry['id']}")
    print(f"Date:    {entry['date']}")
    print(f"Topic:   {entry['topic']}")
    if entry.get("source"):
        print(f"Source:  {entry['source']}")
    if "tags" in entry and entry["tags"]:
        print(f"Tags:    {', '.join(entry['tags'])}")

    if detailed:
        if entry.get("summary"):
            print("\nSummary:")
            print("-" * 40)
            print(entry["summary"])

        if entry.get("details"):
            print("\nDetails:")
            print("-" * 40)
            print(entry["details"])

        print(f"\nCreated:  {entry['created_at']}")
        print(f"Updated:  {entry['updated_at']}")

    print("=" * 80 + "\n")


def search_entries(args):
    """Search for research entries."""
    db = setup_database()
    results = db.search_entries(query=args.query, tag=args.tag, limit=args.limit)

    if not results:
        print("No matching entries found.")
        return

    print(f"\nFound {len(results)} entries:")
    for entry in results:
        print(f"- {entry['date']}: {entry['topic']} (ID: {entry['id']})")
        if args.verbose:
            print_entry(entry, detailed=True)

    if not args.verbose and len(results) > 0:
        print(
            "\nUse --verbose to see full entry details or 'research view ID' to view a specific entry."
        )


def view_entry(args):
    """View a specific research entry by ID."""
    db = setup_database()
    entry = db.get_research_entry(args.entry_id)

    if not entry:
        print(f"No entry found with ID: {args.entry_id}")
        sys.exit(1)

    print_entry(entry, detailed=True)


def add_entry(args):
    """Add a new research entry."""
    db = setup_database()

    entry_data = {
        "id": args.id or f"{datetime.now().strftime('%Y%m%d')}-{hash(datetime.now())}",
        "date": args.date or datetime.now().strftime("%Y-%m-%d"),
        "topic": args.topic,
        "source": args.source or "",
        "summary": args.summary or "",
        "details": args.details or "",
        "tags": [t.strip() for t in args.tags.split(",")] if args.tags else [],
    }

    if db.add_research_entry(entry_data):
        print(f"Successfully added entry with ID: {entry_data['id']}")
        if args.view:
            view_entry(argparse.Namespace(entry_id=entry_data["id"]))
    else:
        print("Failed to add entry.")
        sys.exit(1)


def import_entries(args):
    """Import entries from a JSON file."""
    db = setup_database()
    json_path = Path(args.json_file)

    if not json_path.exists():
        print(f"Error: File not found: {json_path}")
        sys.exit(1)

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            entries = json.load(f)

        if not isinstance(entries, list):
            entries = [entries]

        success_count = 0
        for entry in entries:
            if db.add_research_entry(entry):
                success_count += 1
                if args.verbose:
                    print(
                        f"Imported: {entry.get('id', 'N/A')} - {entry.get('topic', 'No topic')}"
                    )

        print(f"\nSuccessfully imported {success_count}/{len(entries)} entries.")

    except (json.JSONDecodeError, IOError) as e:
        print(f"Error importing from {json_path}: {e}")
        sys.exit(1)


def export_entries(args):
    """Export all entries to a JSON file."""
    db = setup_database()
    entries = db.search_entries(limit=None)  # Get all entries

    if not entries:
        print("No entries to export.")
        return

    output_file = (
        Path(args.output_file) if args.output_file else Path("research_export.json")
    )

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2, ensure_ascii=False, default=str)

        print(f"Successfully exported {len(entries)} entries to {output_file}")

    except IOError as e:
        print(f"Error exporting to {output_file}: {e}")
        sys.exit(1)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Research Management System CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Global arguments
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose output"
    )

    # Subcommands
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Search command
    search_parser = subparsers.add_parser("search", help="Search research entries")
    search_parser.add_argument("query", nargs="?", default="", help="Search query")
    search_parser.add_argument("--tag", help="Filter by tag")
    search_parser.add_argument(
        "--limit", type=int, default=10, help="Maximum number of results"
    )
    search_parser.set_defaults(func=search_entries)

    # View command
    view_parser = subparsers.add_parser("view", help="View a specific entry")
    view_parser.add_argument("entry_id", help="ID of the entry to view")
    view_parser.set_defaults(func=view_entry)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new research entry")
    add_parser.add_argument("--id", help="Entry ID (auto-generated if not provided)")
    add_parser.add_argument("--date", help="Date (YYYY-MM-DD, defaults to today)")
    add_parser.add_argument("--topic", required=True, help="Research topic")
    add_parser.add_argument("--source", help="Source of information")
    add_parser.add_argument("--summary", help="Brief summary")
    add_parser.add_argument("--details", help="Detailed notes")
    add_parser.add_argument("--tags", help="Comma-separated list of tags")
    add_parser.add_argument(
        "--view", action="store_true", help="View the entry after adding"
    )
    add_parser.set_defaults(func=add_entry)

    # Import command
    import_parser = subparsers.add_parser(
        "import", help="Import entries from JSON file"
    )
    import_parser.add_argument("json_file", help="Path to JSON file to import")
    import_parser.add_argument(
        "--verbose", "-v", action="store_true", help="Show import progress"
    )
    import_parser.set_defaults(func=import_entries)

    # Export command
    export_parser = subparsers.add_parser("export", help="Export all entries to JSON")
    export_parser.add_argument(
        "--output", "-o", dest="output_file", help="Output file path"
    )
    export_parser.set_defaults(func=export_entries)

    # Parse arguments and execute the appropriate function
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    try:
        args.func(args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
