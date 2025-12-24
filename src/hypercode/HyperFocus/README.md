# HyperFocus

Bulk automate your GitHub repositories with neurodivergent-friendly power.

## Features

- Scans all your git repos automatically
- Detects programming language per repo
- Generates intelligent READMEs using AI
- Adds .gitignore and LICENSE files
- Commits and pushes in parallel
- Learns your preferences
- Supports 14+ programming ecosystems
- Works offline with templates

## Quick Start

### Installation

```bash
pip install hyperfocus
```

### Setup

```bash
hyperfocus setup
```

Answer the interactive prompts:
- Path to your repos directory
- GitHub username
- Default license type
- Preferred template

### Run

```bash
hyperfocus run
```

Options:
```bash
hyperfocus run --repos ~/Dev --github MyUser --push
hyperfocus run --dry-run  # Preview before committing
hyperfocus run -s HyperCode -s PennyPet  # Select specific repos
```

### Check Status

```bash
hyperfocus status
hyperfocus logs
```

## Commands

- `setup` - Configure HyperFocus
- `run` - Process your repos
- `status` - Show current config
- `logs` - View recent runs
- `reset` - Clear all settings

## Supported Ecosystems

- Python (pip, pyproject.toml)
- JavaScript/Node.js (npm, yarn)
- TypeScript
- Rust (cargo)
- Go
- Java
- C#/.NET
- C++
- HyperCode
- AI/ML
- DevOps
- And more...

## Configuration

Config saved to `~/.hyperfocus/config.json`

Example:
```json
{
  "github_user": "YourUsername",
  "default_repos_path": "/home/user/Dev",
  "default_license": "MIT",
  "default_ecosystem": "multiverse",
  "auto_push": false,
  "parallel_workers": 5,
  "template": "neurodivergent-friendly"
}
```

## Environment Variables

Create `.env` file:
```
PERPLEXITY_API_KEY=your_key_here
GITHUB_TOKEN=your_token_here
```

## Development

```bash
git clone https://github.com/YourUsername/hyperfocus
cd hyperfocus
pip install -e .
hyperfocus setup
hyperfocus run --dry-run
```

## License

MIT License - See LICENSE file

## Made with love for neurodivergent developers
