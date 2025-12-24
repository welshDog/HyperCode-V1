# HyperCode Project Organization

This directory contains tools for organizing the HyperCode project structure.

## Main Script

- `project_organizer.py` - The primary script for organizing project files and documentation
  - Features:
    - Dry-run mode for previewing changes
    - Comprehensive logging
    - Handles both file organization and documentation
    - Preserves file structure while moving items

## Usage

```bash
# Basic usage
python project_organizer.py

# Preview changes without making them
python project_organizer.py --dry-run

# Get help
python project_organizer.py --help
```

## Archived Scripts

The `archive/` directory contains older organization scripts that have been superseded by `project_organizer.py`:
- `organize_moved_files.ps1` - Initial PowerShell script for basic file organization
- `organize_repo.ps1` - Alternative PowerShell script with different organization logic
- `reorganize_repo.py` - Python script focused on repository restructuring

## Best Practices

1. Always run with `--dry-run` first to preview changes
2. Check the `project_organizer.log` for detailed operation logs
3. Commit or backup your repository before running organization scripts
