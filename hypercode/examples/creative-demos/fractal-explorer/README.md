# 🌀 HyperCode Fractal Explorer

An interactive fractal visualization tool built with HyperCode, showcasing the language's capabilities for mathematical computing and visual programming.

![Fractal Explorer Screenshot](screenshot.png)

## ✨ Features

- **Multiple Fractal Types**: Mandelbrot, Julia, and more
- **Interactive Zoom**: Click and drag to explore infinite detail
- **Color Palettes**: Multiple color schemes to choose from
- **Performance Optimized**: Fast rendering with WebAssembly
- **Keyboard Controls**: Intuitive navigation and adjustments

## 🚀 Getting Started

### Prerequisites
- HyperCode Runtime (v1.0.0 or later)
- Modern web browser with WebAssembly support

### Running the Demo

1. Clone the repository:
   ```bash
   git clone https://github.com/welshDog/hypercode.git
   cd hypercode/showcase/creative-demos/fractal-explorer
   ```

2. Start the development server:
   ```bash
   npm install
   npm run dev
   ```

3. Open your browser to `http://localhost:3000`

## 🛠️ Development

### Project Structure
```
fractal-explorer/
├── src/
│   ├── fractals/     # Fractal algorithms
│   ├── renderer/     # WebGL/Canvas rendering
│   ├── ui/           # User interface components
│   └── main.hc       # Main application
├── assets/          # Images, shaders, etc.
└── tests/           # Unit tests
```

### Available Scripts
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm test` - Run tests
- `npm run lint` - Lint code

## 📚 Learn More

- [HyperCode Documentation](https://welshdog.github.io/hypercode)
- [Fractal Mathematics](https://en.wikipedia.org/wiki/Fractal)
- [WebGL Guide](https://webglfundamentals.org/)

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) to get started.

## 📄 License

This project is [MIT licensed](LICENSE).
