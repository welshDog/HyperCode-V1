# 🎨 HyperCode Visual Syntax - VS Code Extension

## 🌟 Visual Semantic Syntax Highlighting for Neurodivergent Developers

**HyperCode Visual Syntax** is a VS Code extension that provides emoji-based semantic annotations and visual syntax highlighting specifically designed for neurodivergent developers. This extension makes code more readable, accessible, and cognitively friendly through visual markers and semantic context.

## ✨ Features

### 🎯 **Semantic Annotations**
- **Visual markers** using emojis for different code concepts
- **Auto-completion** for semantic annotations
- **Hover information** explaining each annotation
- **Real-time parsing** and validation

### 🧠 **Neurodiversity-First Design**
- **Reduced cognitive load** through visual clarity
- **Color-coded comments** for better organization
- **Consistent visual patterns** for predictability
- **Accessibility-focused** interface design

### 🔤 **Supported Annotations**
- `🎯 @verifiable(...)` - Formal verification and proof annotations
- `✅ @ensures(...)` - Postconditions and guarantees  
- `📋 @requires(...)` - Preconditions and dependencies
- `💡 @intent(...)` - Purpose and cognitive context
- `♿ @accessibility(...)` - Neurodiversity and inclusive design
- `⚡ @computation(...)` - Computational complexity and behavior
- `⚙️ @operation(...)` - Runtime operations and side effects
- `📤 @return(...)` - Return value specifications

## 🚀 Installation

### From VS Code Marketplace
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "HyperCode Visual Syntax"
4. Click Install

### From VSIX (Manual)
1. Download the latest `.vsix` file from [Releases](https://github.com/welshDog/hypercode/releases)
2. In VS Code: `Extensions > Install from VSIX...`
3. Select the downloaded file

## 📖 Usage

### Adding Semantic Annotations

```python
# 🎯 @verifiable("This function is mathematically verified")
def calculate_factorial(n: int) -> int:
    # 📋 @requires("n >= 0")
    # ✅ @ensures("return value is n!")
    
    if n <= 1:
        return 1
    
    # ⚡ @computation("O(n) time complexity")
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    # 📤 @return("factorial of n")
    return result

# 💡 @intent("Demonstrates recursive pattern matching")
# ♿ @accessibility("Clear visual structure with emoji markers")
def process_data(data: list[str]) -> dict[str, int]:
    # ⚙️ @operation("Transforms list to frequency dictionary")
    pass
```

### Auto-Completion
Type `@` in a Python or HyperCode file to see available semantic annotations.

### Hover Information
Hover over any semantic annotation to see detailed explanations and usage guidelines.

## ⚙️ Configuration

The extension can be configured through VS Code settings:

```json
{
  "hypercode.semanticHighlighting": true,
  "hypercode.neurodiversityMode": true, 
  "hypercode.realtimeParsing": true
}
```

### Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `hypercode.semanticHighlighting` | boolean | true | Enable visual semantic syntax highlighting |
| `hypercode.neurodiversityMode` | boolean | true | Enable neurodiversity-focused visual enhancements |
| `hypercode.realtimeParsing` | boolean | true | Enable real-time parsing and validation |

## 🎨 Supported Languages

- **Python** (Full semantic annotation support)
- **HyperCode** (Native language support)
- **Any language** with comment support (basic emoji highlighting)

## 🔧 Development

### Prerequisites
- Node.js 18+
- npm or yarn
- TypeScript 5+

### Setup
```bash
# Clone the repository
git clone https://github.com/welshDog/hypercode.git
cd hypercode/vscode-extension

# Install dependencies
npm install

# Compile TypeScript
npm run compile

# Watch for changes
npm run watch
```

### Building
```bash
# Compile for production
npm run vscode:prepublish

# Package extension
vsce package
```

### Testing
```bash
# Start development mode
code --extensionDevelopmentPath=. .
```

## 🌟 Why HyperCode Visual Syntax?

### 🧠 **Neurodivergent Accessibility**
- **Visual clarity** reduces cognitive load
- **Emoji markers** provide instant visual context
- **Consistent patterns** reduce mental overhead
- **Color coding** aids visual organization

### 📚 **Semantic Understanding**
- **Intent markers** explain code purpose
- **Complexity indicators** help with performance decisions
- **Verification tags** ensure code reliability
- **Accessibility notes** promote inclusive design

### 🚀 **Developer Experience**
- **Auto-completion** speeds up annotation
- **Hover info** provides instant context
- **Real-time validation** catches errors early
- **Visual feedback** enhances code comprehension

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](../../CONTRIBUTING.md) for details.

### Development Focus Areas
- 🎨 New semantic annotation types
- 🧠 Additional accessibility features  
- 🔌 Integration with other tools
- 📚 Expanded language support

## 📄 License

MIT License - see [LICENSE](../../LICENSE) file for details.

## 🔗 Links

- **Main Project**: [HyperCode](https://github.com/welshDog/hypercode)
- **Documentation**: [HyperCode Docs](https://docs.hypercode.dev)
- **Community**: [Discord](https://discord.gg/hypercode)
- **Issues**: [GitHub Issues](https://github.com/welshDog/hypercode/issues)

## 🙏 Acknowledgments

Special thanks to the neurodivergent developer community for feedback and insights that shaped this extension's design.

---

**Made with ❤️ for neurodivergent developers everywhere**
