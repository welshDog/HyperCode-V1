# HyperCode Developer Guide

This guide provides information for developers working on the HyperCode project.

## Project Structure

```
hypercode-v2/
├── docs/                 # Documentation
├── src/                  # Source code
├── tests/                # Test files
├── scripts/              # Utility scripts
└── examples/             # Example code
```

## Development Setup

1. **Prerequisites**
   - Python 3.10+
   - Node.js (for frontend components)
   - PostgreSQL (for database)

2. **Install Dependencies**
   ```bash
   # Python dependencies
   pip install -r requirements-dev.txt
   
   # Frontend dependencies
   cd frontend
   npm install
   ```

3. **Environment Setup**
   Copy the example environment file and update with your configuration:
   ```bash
   cp .env.example .env
   ```

## Database Management

### Schema Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "description of changes"

# Apply migrations
alembic upgrade head
```

### Database Backups

```bash
# Create backup
pg_dump hypercode_db > backup_$(date +%Y%m%d).sql

# Restore from backup
psql hypercode_db < backup_20231221.sql
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_module.py

# Run with coverage report
pytest --cov=src --cov-report=html
```

## Code Style

- Follow PEP 8 for Python code
- Use type hints for all function signatures
- Document all public functions and classes with docstrings
- Keep functions small and focused (under 50 lines)

## Commit Guidelines

- Use conventional commit messages:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `style:` for formatting changes
  - `refactor:` for code refactoring
  - `test:` for test changes
  - `chore:` for maintenance tasks

Example:
```
feat: add user authentication

- Implement JWT token generation
- Add login/logout endpoints
- Update documentation
```

## Documentation

Keep documentation up to date. When making changes:

1. Update relevant docstrings
2. Update README files if needed
3. Add/update examples

## Pull Requests

1. Create a feature branch from `main`
2. Make your changes
3. Write tests for new features
4. Update documentation
5. Run tests and ensure they pass
6. Submit a pull request with a clear description

## Code Review Process

1. At least one approval required before merging
2. Address all review comments
3. Update documentation if needed
4. Ensure all tests pass

## Deployment

### Staging
Merging to `staging` branch triggers a deployment to the staging environment.

### Production
Create a release in GitHub to deploy to production.

## Getting Help

- Check the [FAQ](FAQ.md)
- Open an issue for bugs or feature requests
- Join our [community chat](https://chat.example.com)

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
