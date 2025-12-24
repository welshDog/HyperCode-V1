#!/usr/bin/env python3
"""
HyperCode Space-to-Main Sync Script
Mirrors Space export data (docs, data, assets) into main repo folders.
One-way sync with logging, conflict resolution, and dry-run mode.

Usage:
    python scripts/sync-space-to-main.py                  # Full sync
    python scripts/sync-space-to-main.py --dry-run        # Preview changes
    python scripts/sync-space-to-main.py --config custom.toml  # Custom config
"""

import argparse
import json
import os
import shutil  # type: ignore
import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

import toml


def log_error(msg: str):
    """Error-level log with traceback."""
    print(f"{Colors.RED}[ERROR]{Colors.RESET} {msg}")
    exc_type, exc_value, exc_traceback = sys.exc_info()
    if exc_type:
        print(f"{Colors.RED}Exception Type: {exc_type.__name__}{Colors.RESET}")
        print(f"{Colors.RED}Exception Value: {exc_value}{Colors.RESET}")
        print(f"{Colors.YELLOW}Traceback:{Colors.RESET}")
        traceback.print_tb(exc_traceback)


# ANSI colors for terminal output
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


def log_info(msg: str):
    """Info-level log."""
    print(f"{Colors.BLUE}[INFO]{Colors.RESET} {msg}")


def log_success(msg: str):
    """Success-level log."""
    print(f"{Colors.GREEN}[✓]{Colors.RESET} {msg}")


def log_warning(msg: str):
    """Warning-level log."""
    print(f"{Colors.YELLOW}[⚠]{Colors.RESET} {msg}")


def deep_merge(source: Dict, destination: Dict) -> Dict:
    """Recursively merge source dict into destination dict."""
    for key, value in source.items():
        if isinstance(value, dict):
            node = destination.setdefault(key, {})
            deep_merge(value, node)
        else:
            destination[key] = value
    return destination


def load_config(config_path: str = ".hypercode/sync.toml") -> Dict:
    """
    Load sync configuration from TOML file.
    Fallback to defaults if file doesn't exist.
    """
    default_config = {
        "sync": {
            "source_root": "space_sync",
            "target_root": ".",
            "mappings": {
                "raw_docs": "docs",
                "raw_data": "data",
                "raw_assets": "assets",
            },
            "strict_mirror": False,
            "delete_orphans": False,
            "preserve_patterns": [".git", ".gitignore", "*.md", "README*"],
            "log_file": "logs/sync-space-to-main.log",
        },
        "filters": {
            "exclude_extensions": [".tmp", ".bak", ".swp"],
            "exclude_dirs": ["__pycache__", ".pytest_cache", "node_modules"],
            "exclude_names": [".DS_Store", "Thumbs.db"],
        },
    }

    if os.path.exists(config_path):
        try:
            user_config = toml.load(config_path)
            deep_merge(user_config, default_config)
            log_success(f"Loaded config from {config_path}")
        except Exception as e:
            log_error(f"Failed to parse {config_path}: {e}")
            log_warning("Falling back to default configuration")
    else:
        log_warning(f"Config file {config_path} not found, using defaults")

    return default_config


def should_skip_file(filepath: Path, config: Dict) -> bool:
    """Check if file should be skipped based on filters."""
    filters = config.get("filters", {})
    exclude_ext = filters.get("exclude_extensions", [])
    exclude_dirs = filters.get("exclude_dirs", [])
    exclude_names = filters.get("exclude_names", [])

    # Check extension
    if filepath.suffix in exclude_ext:
        return True

    # Check filename
    if filepath.name in exclude_names:
        return True

    # Check if any parent dir is excluded
    for part in filepath.parts:
        if part in exclude_dirs:
            return True

    return False


def get_all_files(directory: Path) -> List[Path]:
    """Recursively get all files in directory."""
    files = []
    if directory.exists():
        for item in directory.rglob("*"):
            if item.is_file():
                files.append(item)
    return files


def copy_file(src: Path, dst: Path, dry_run: bool = False) -> bool:
    """Copy file with directory creation. Returns True if copied/would copy."""
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dry_run:
            shutil.copy2(src, dst)
        return True
    except Exception as e:
        log_error(f"Failed to copy {src} → {dst}: {e}")
        return False


def remove_file(filepath: Path, dry_run: bool = False) -> bool:
    """Remove file. Returns True if removed/would remove."""
    try:
        if not dry_run:
            filepath.unlink()
        return True
    except Exception as e:
        log_error(f"Failed to delete {filepath}: {e}")
        return False


def sync_folder(
    source: Path, target: Path, config: Dict, dry_run: bool = False
) -> Tuple[int, int, int]:
    """
    Sync source folder to target folder (one-way).
    Returns (copied, updated, errors) counts.
    """
    copied, updated, errors = 0, 0, 0

    if not source.exists():
        log_warning(f"Source folder {source} doesn't exist, skipping")
        return copied, updated, errors

    source_files = get_all_files(source)

    for src_file in source_files:
        if should_skip_file(src_file, config):
            continue

        # Calculate relative path and target location
        rel_path = src_file.relative_to(source)
        tgt_file = target / rel_path

        # Check if target exists and is newer (update scenario)
        if tgt_file.exists():
            src_mtime = os.path.getmtime(src_file)
            tgt_mtime = os.path.getmtime(tgt_file)

            if src_mtime > tgt_mtime:
                if copy_file(src_file, tgt_file, dry_run):
                    log_info(f"Updated: {rel_path}")
                    updated += 1
                else:
                    errors += 1
        else:
            if copy_file(src_file, tgt_file, dry_run):
                log_info(f"Copied: {rel_path}")
                copied += 1
            else:
                errors += 1

    return copied, updated, errors


def delete_orphans(target: Path, source: Path, dry_run: bool = False) -> int:
    """Remove files from target that no longer exist in source."""
    deleted = 0
    target_files = get_all_files(target)

    for tgt_file in target_files:
        rel_path = tgt_file.relative_to(target)
        src_file = source / rel_path

        if not src_file.exists():
            if remove_file(tgt_file, dry_run):
                log_info(f"Deleted orphan: {rel_path}")
                deleted += 1

    return deleted


def sync_all_mappings(config: Dict, dry_run: bool = False) -> Dict:
    """Execute all mappings from config."""
    sync_config = config.get("sync", {})
    source_root = Path(sync_config.get("source_root", "space_sync")).resolve()
    target_root = Path(sync_config.get("target_root", ".")).resolve()

    # Only include string values in mappings (exclude boolean/list config values)
    mappings = {
        k: v for k, v in sync_config.get("mappings", {}).items() if isinstance(v, str)
    }
    delete_orphans_flag = sync_config.get("delete_orphans", False)

    stats = {
        "total_copied": 0,
        "total_updated": 0,
        "total_deleted": 0,
        "total_errors": 0,
        "mappings": {},
    }

    log_info(f"Starting sync: {source_root} → {target_root}")
    if dry_run:
        log_warning("DRY RUN MODE (no files will be modified)")

    for source_name, target_name in mappings.items():
        source = source_root / str(source_name)
        target = target_root / str(target_name)

        if not source.exists():
            log_warning(f"Source folder {source} doesn't exist, skipping")
            continue

        log_info(f"Syncing: {source_name} → {target_name}")

        copied, updated, errors = sync_folder(source, target, config, dry_run)
        stats["total_copied"] += copied
        stats["total_updated"] += updated
        stats["total_errors"] += errors
        stats["mappings"][source_name] = {
            "target": target_name,
            "copied": copied,
            "updated": updated,
            "errors": errors,
        }

        if delete_orphans_flag:
            deleted = delete_orphans(target, source, dry_run)
            stats["total_deleted"] += deleted

    return stats


def write_log(log_file: str, stats: Dict, dry_run: bool = False):
    """Write sync results to log file."""
    log_dir = Path(log_file).parent
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().isoformat()
    mode = "[DRY RUN]" if dry_run else "[LIVE]"

    try:
        with open(log_file, "a") as f:
            f.write(f"\n{'-' * 60}\n")
            f.write(f"{timestamp} {mode}\n")
            f.write(
                f"Copied: {stats['total_copied']} | Updated: {stats['total_updated']} | "
                f"Deleted: {stats['total_deleted']} | Errors: {stats['total_errors']}\n"
            )
            f.write(json.dumps(stats.get("mappings", {}), indent=2) + "\n")
        log_success(f"Log written to {log_file}")
    except Exception as e:
        log_error(f"Failed to write log: {e}")


def print_summary(stats: Dict, dry_run: bool = False):
    """Print sync summary to console."""
    print("\n" + "=" * 80)
    print(f"{'SYNC SUMMARY' + (' (DRY RUN)' if dry_run else ''):^80}")
    print("=" * 80)
    print(f"Copied: {stats['total_copied']}")
    print(f"Updated: {stats['total_updated']}")
    print(f"Deleted: {stats['total_deleted']}")
    print(f"Errors: {stats['total_errors']}\n")

    print("Mapping Details:")
    for src, details in stats["mappings"].items():
        tgt = details.get("target", "")
        print(
            f"  {str(src)[:20]:20} → {str(tgt)[:20]:20} (copied: {details['copied']}, "
            f"updated: {details['updated']}, errors: {details['errors']}"
        )

    if dry_run:
        print("\n" + "=" * 80)
        print("NOTE: This was a dry run. No files were actually modified.")
    print("=" * 80)


def main():
    try:
        parser = argparse.ArgumentParser(
            description="HyperCode Space-to-Main Sync: Mirror Space exports into repo folders."
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Preview changes without modifying files",
        )
        parser.add_argument(
            "--config",
            default=".hypercode/sync.toml",
            help="Path to sync config file (default: .hypercode/sync.toml)",
        )

        args = parser.parse_args()

        # Load configuration
        config = load_config(args.config)

        # Execute sync
        stats = sync_all_mappings(config, dry_run=args.dry_run)

        # Log results
        log_file = config.get("sync", {}).get("log_file", "logs/sync-space-to-main.log")
        write_log(log_file, stats, dry_run=args.dry_run)

        # Print summary
        print_summary(stats, dry_run=args.dry_run)

        # Exit with error code if there were errors
        sys.exit(1 if stats["total_errors"] > 0 else 0)
    except Exception as e:
        log_error(f"Fatal error during sync: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
