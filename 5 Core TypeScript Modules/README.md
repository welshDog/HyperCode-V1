# 🧠 Windsurf Spatial Code Visualizer

**A neurodivergent-friendly spatial code visualization extension for Windsurf IDE**

Turns your code into interactive mind-maps, force-directed graphs, and hierarchical
visualizations that reduce cognitive load and boost hyperfocus productivity.

---

## 🎯 What It Does

- **Spatial Mind-Map Visualization**: Renders code structure as interactive mind-maps
  (default)
- **Multiple Layout Modes**: Switch between mind-map, force-directed, hierarchical, and
  radial layouts
- **Cognitive Load Scoring**: Analyzes and displays code complexity in real-time
- **Language Support**: Python, JavaScript, TypeScript (extensible)
- **ADHD-Friendly UX**: Minimal noise, high clarity, zero context-switching
- **Accessibility First**: Designed for neurodivergent brains (ADHD, autism, dyslexia)
- **Real-Time Analysis**: Updates as you code
- **Export to SVG**: Save visualizations for documentation

---

## 🚀 Installation

### Prerequisites

- Windsurf IDE (or VS Code with compatibility layer)
- Node.js 18+
- npm or yarn

### Setup

```bash
# Clone the repo
git clone https://github.com/hypercode-dev/windsurf-spatial-visualizer.git
cd windsurf-spatial-visualizer

# Install dependencies
npm install

# Build the extension
npm run build

# For development with watch mode
npm run watch
```

### Load into Windsurf

1. Open Windsurf
2. Press `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Linux/Windows)
3. Type: `Extensions: Install from VSIX`
4. Select the built `.vsix` file from `dist/`

Or use `vsce`:

```bash
npx vsce package
```

---

## 📖 Usage

### Open Spatial Visualizer

1. Open any Python or JavaScript file
2. Press `Ctrl+Shift+V` (or `Cmd+Shift+V` on macOS)
3. The visualizer opens in a side panel with multiple views:

**Visualization Modes:**

- **Mind-Map** (default): Concentric circles of functions, classes, imports
- **Force-Directed**: Physics-based node positioning (good for dependency analysis)
- **Hierarchical**: Top-down tree layout
- **Radial**: Radial burst from center

### Features

**Toggle Visualization Mode**

```
Ctrl+Shift+P → "Spatial Visualizer: Toggle Mode"
```

**Cognitive Load Scoring**

- Each node shows cognitive complexity via visual ring intensity
- Overall score: 1-10 scale
- High-load areas highlighted in red

**Click Nodes** (in webview)

- Jump to source code location
- View node details (complexity, dependencies, line number)

**Export Visualization**

- Button in header exports current view as SVG
- Use for documentation, presentations, or team sharing

---

## 🧠 How It Works

### 1. **Code Analysis Phase**

- Parser scans code for functions, classes, imports, interfaces
- Calculates cyclomatic complexity per function
- Measures cognitive load (nesting depth, line length, parameter count)
- Extracts function call dependencies

### 2. **Spatial Mapping Phase**

- Maps code elements to spatial positions based on visualization mode
- Assigns colors by type (function=indigo, class=pink, variable=green, etc.)
- Encodes complexity as visual ring intensity

### 3. **Rendering Phase**

- D3.js renders interactive SVG visualization
- CSS ensures accessibility (high contrast, minimal animation)
- Real-time updates as code changes

---

## 🎨 Color Scheme

Designed for accessibility (WCAG AA+):

| Type                | Color             | Meaning                 |
| ------------------- | ----------------- | ----------------------- |
| Function            | Indigo (#6366f1)  | Logic entry points      |
| Class               | Pink (#ec4899)    | Object definitions      |
| Variable            | Emerald (#10b981) | Data holders            |
| Import              | Amber (#f59e0b)   | External dependencies   |
| Interface           | Violet (#8b5cf6)  | Type contracts          |
| Cognitive Load Ring | Red (#ef4444)     | High complexity warning |

---

## ⚡ Performance

- **Analysis Time**: < 500ms for files up to 10K lines
- **Render Time**: < 200ms with D3.js
- **Memory**: ~5-10MB per analysis

For larger codebases, use **workspace filtering**:

```typescript
// Analyze only specific folder
const analyzer = new CodeAnalyzer({ basePath: "src/" });
```

---

## 🔧 Configuration

Create a `.visualizer.json` in your workspace root:

```json
{
  "defaultMode": "mindmap",
  "minimalNoise": true,
  "highContrast": false,
  "excludePatterns": ["node_modules/**", "dist/**", "*.test.ts"],
  "cognitiveLoadThreshold": 7,
  "updateDebounce": 500,
  "colors": {
    "function": "#6366f1",
    "class": "#ec4899"
  }
}
```

---

## 📚 Supported Languages

**Fully Supported:**

- Python
- JavaScript
- TypeScript

**Partial Support:**

- Go
- Rust
- Java

**Contributing:** Add language support via `code-analyzer.ts`:

```typescript
private analyzeYourLanguage(code: string): CodeAnalysis {
  // Implement parser + node extraction
}
```

---

## 🧑‍💻 Development

### Project Structure

```
windsurf-spatial-visualizer/
├── src/
│   ├── extension.ts              # Main entry + command registration
│   ├── code-analyzer.ts          # AST parsing + complexity calculation
│   ├── spatial-visualizer.ts     # D3.js visualization engine
│   ├── visualization-panel.ts    # VS Code webview + UI
│   └── types.ts                  # TypeScript interfaces
├── dist/                         # Compiled output
├── package.json
├── tsconfig.json
├── webpack.config.js
└── README.md
```

### Build Commands

```bash
npm run build        # Compile TypeScript + webpack
npm run watch        # Watch mode (dev)
npm run test         # Run jest tests
npm run lint         # ESLint
```

### Testing

```bash
# Run all tests
npm test

# Watch tests
npm test -- --watch

# Coverage report
npm test -- --coverage
```

---

## 🤝 Contributing

We love contributions! Especially from neurodivergent developers.

**Steps:**

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -am 'Add amazing feature'`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

**Areas we need help:**

- Additional language parsers
- Accessibility improvements
- Performance optimization
- UI/UX refinements
- Documentation

---

## 🛠️ Troubleshooting

### "Visualizer doesn't open"

- Ensure a code file is active in the editor
- Try reloading the extension: `Cmd+R` (macOS) or `Ctrl+R` (Windows/Linux)

### "Analysis takes too long"

- File might be too large. Try analyzing a smaller section
- Increase `updateDebounce` in config

### "Colors aren't accessible enough"

- Toggle **Toggle Contrast** button in header
- Report accessibility issues: issues@hypercode.dev

---

## 📄 License

MIT © 2025 HyperCode Team

---

## 🎓 Research & Inspiration

Built on decades of research into:

- **Neurodivergent cognition** (ADHD, autism, dyslexia)
- **Spatial memory systems** (hippocampus-based learning)
- **Flow state psychology** (Csikszentmihalyi)
- **Esoteric languages** (Brainfuck, Befunge mind-map roots)

**Citation:** If you use this in research or teaching, please cite:

```
HyperCode Team. (2025). Windsurf Spatial Code Visualizer.
GitHub: https://github.com/hypercode-dev/windsurf-spatial-visualizer
```

---

## 💬 Support

- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Email**: support@hypercode.dev
- **Discord**: Join our community server

---

## 🚀 Roadmap

- [ ] AI-powered refactoring suggestions
- [ ] Real-time pair programming sync
- [ ] Custom visualization themes
- [ ] Integration with HyperCode language
- [ ] Mobile companion app
- [ ] Collaborative visualization sharing
- [ ] VR code visualization mode

---

**Ready to code spatially? Let's hyperfocus! 🧠✨**

_Made by neurodivergent developers, for neurodivergent developers._
