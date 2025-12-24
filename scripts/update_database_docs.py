#!/usr/bin/env python3
"""
Update HyperCode Database Documentation

This script generates and updates the database documentation.
"""

import datetime
from pathlib import Path


def generate_database_docs():
    """Generate database documentation."""
    content = f"""# 🧠 HyperCode Database Documentation

Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview
This document provides an overview of the HyperCode database structure and usage.

## Database Schema

### Core Tables

1. **knowledge_nodes**
   - Stores core knowledge entities
   - Fields: id, type, name, content, metadata, created_at, updated_at

2. **relationships**
   - Stores relationships between knowledge nodes
   - Fields: id, source_id, target_id, type, weight, metadata

3. **documents**
   - Stores document content and metadata
   - Fields: id, title, content_type, content, metadata, created_at

## Usage Examples

```python
# Example query to get related nodes
def get_related_nodes(node_id, relationship_type=None):
    """Get nodes related to the given node.
    
    Args:
        node_id: The ID of the node to find relationships for
        relationship_type: Optional filter for relationship type
        
    Returns:
        List of related nodes
    """
    # Implementation here
    pass
```

## Maintenance

### Backup
```bash
# Create backup
pg_dump hypercode_db > backup_$(date +%Y%m%d).sql
```

### Performance
- Regular vacuum and analyze recommended
- Consider adding indexes for frequently queried fields

## Next Steps
- [ ] Document all database views
- [ ] Add data validation rules
- [ ] Document replication setup
"""
    
    # Save to file
    docs_dir = Path("docs/database")
    docs_dir.mkdir(exist_ok=True)
    with open(docs_dir / "DATABASE.md", "w") as f:
        f.write(content)
    
    print(f"✅ Database documentation generated at {docs_dir / 'DATABASE.md'}")

if __name__ == "__main__":
    generate_database_docs()
