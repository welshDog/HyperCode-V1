# HyperCode Contribution Guidelines

## First Time Contributors

- Look for issues labeled `good first issue`
- Join our [Discord](https://discord.gg/hypercode) for real-time help
- Check out the [Beginner's Guide](docs/beginner-guide.md)

## Development Setup

```bash
git clone https://github.com/welshDog/hypercode.git
cd hypercode
pip install -e ".[dev]"
pre-commit install
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Add tests for your changes
4. Run `make test` and `make lint`
5. Submit a PR with a clear description

## Code Style

- Follow PEP 8
- Use type hints
- Document public APIs
- Write docstrings in Google style
