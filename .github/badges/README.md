# 🏆 HyperCode Badge System

## Badge Assets

This directory contains the visual assets for HyperCode contributor recognition badges.

### Badge Files

- `badge_first_commit.png` - 🚀 Electric Blue Rocket (First PR merged)
- `badge_code_contrib.png` - 🔥 Orange-Red Flame (5+ PRs merged)
- `badge_accessibility.png` - ♿ Purple Access + Brain (3+ A11y PRs)
- `badge_ai_architect.png` - 🤖 Cyan Robot (AI/Python work)
- `badge_doc_hero.png` - 📚 Green Book Star (5+ Doc PRs)
- `badge_design_wizard.png` - 🎨 Pink Magic Wand (UI/Design work)
- `badge_hyperfocus_legend.png` - ⭐ Gold Star Infinity (50+ commits)

### Design Specifications

- **Format**: PNG with transparency
- **Size**: 128x128px (scalable)
- **Style**: Rounded hexagons, high contrast (4.5:1+)
- **Accessibility**: Dyslexia-friendly, sans-serif typography

### Usage

Badges are automatically assigned via GitHub Actions workflow:

- `.github/workflows/assign-badges.yml`
- Updates README.md contributor section
- Comments on PRs when badges are earned

### Integration

Referenced in:

- `README.md` - Badge gallery and contributor table
- `CONTRIBUTING.md` - Badge earning criteria
- GitHub Actions - Automatic assignment logic
