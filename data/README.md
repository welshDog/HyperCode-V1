# Data Directory Structure

This directory contains research data, database files, and related resources for the HyperCode project.

## 📁 Directory Structure

```text
data/
├── processed/           # Processed data files (cleaned, transformed)
├── reseach data json/   # Raw research data in JSON format
├── space_sync/          # Space-related synchronization data
├── DATABASE_GUIDE.md    # Database usage and schema documentation
├── INSTALLATION_GUIDE.txt  # Setup instructions
├── PYPROJECT_ADDITIONS.txt # Project configuration additions
├── SYSTEM_SETUP_SUMMARY.txt # System setup summary
├── cli_main.py         # Command-line interface
├── db.py               # Database connection and operations
├── models.py           # Database models
├── research_agent.py   # Research data processing agent
├── research_database.db  # SQLite database file
└── test_data.json      # Sample test data
```

## 🗄️ Database Information

### Schema Overview

- **research_papers**: Stores research paper metadata and content
- **code_examples**: Code snippets with metadata
- **concepts**: Key programming concepts
- **relationships**: Connections between concepts and papers

### Database Management

- **File**: `research_database.db` (SQLite)
- **Documentation**: See [DATABASE_GUIDE.md](DATABASE_GUIDE.md)
- **Models**: Defined in `models.py`

## 🔄 Data Processing

### Raw Data

- Location: `reseach data json/`
- Format: JSON files containing research data

### Processed Data

- Location: `processed/`
- Cleaned and transformed data ready for analysis

## 🛠️ Usage

### Setup

1. Follow instructions in [INSTALLATION_GUIDE.txt](INSTALLATION_GUIDE.txt)
2. Configure database connection in `db.py` if needed
3. Run `research_agent.py` to process new data

### CLI

Use the command-line interface for common tasks:

```bash
python data/cli_main.py [command] [options]
```

## 📊 Data Dictionary

### research_papers

- `id`: Unique identifier
- `title`: Paper title
- `authors`: List of authors
- `publication_date`: Publication date
- `abstract`: Paper abstract
- `content`: Full text content
- `url`: Source URL
- `keywords`: List of keywords

### code_examples

- `id`: Unique identifier
- `content`: Source code
- `language`: Programming language
- `paper_id`: Reference to source paper
- `description`: Code description

## 🔒 Data Privacy

- Do not commit sensitive information
- Anonymize data when necessary
- Follow project's data retention policies

## 📈 Maintenance

- Regularly back up the database
- Document any schema changes
- Keep raw data files for reproducibility

---
*Last Updated: December 2025*
