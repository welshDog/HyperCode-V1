// fractal.hc - A simple fractal explorer in HyperCode

// Import necessary libraries
import { Canvas, Color } from 'hypercode/graphics'
import { Vec2 } from 'hypercode/math'

// Fractal types
enum FractalType {
    MANDELBROT = 'mandelbrot',
    JULIA = 'julia',
    BURNING_SHIP = 'burning_ship'
}

// Color palette generator
class ColorPalette {
    static generatePalette(iterations: number): Color[] {
        const palette: Color[] = []
        for (let i = 0; i < iterations; i++) {
            // Generate a smooth color gradient
            const t = i / iterations
            const r = Math.floor(9 * (1 - t) * t * t * t * 255)
            const g = Math.floor(15 * Math.pow(1 - t, 2) * Math.pow(t, 2) * 255)
            const b = Math.floor(8.5 * Math.pow(1 - t, 3) * t * 255)
            palette.push(new Color(r, g, b, 255))
        }
        return palette
    }
}

// Base fractal class
abstract class Fractal {
    maxIterations: number
    escapeRadius: number
    palette: Color[]

    constructor(maxIterations: number = 100) {
        this.maxIterations = maxIterations
        this.escapeRadius = 2.0
        this.palette = ColorPalette.generatePalette(maxIterations)
    }

    abstract computePoint(x: number, y: number): number

    getColor(iterations: number): Color {
        if (iterations >= this.maxIterations) {
            return Color.BLACK
        }
        return this.palette[iterations % this.palette.length]
    }
}

// Mandelbrot set implementation
class Mandelbrot extends Fractal {
    computePoint(x0: number, y0: number): number {
        let x = 0.0
        let y = 0.0
        let iteration = 0
        
        while (x * x + y * y < this.escapeRadius * this.escapeRadius && 
               iteration < this.maxIterations) {
            const xtemp = x * x - y * y + x0
            y = 2 * x * y + y0
            x = xtemp
            iteration++
        }
        
        return iteration
    }
}

// Fractal renderer
class FractalRenderer {
    canvas: Canvas
    fractal: Fractal
    zoom: number = 1.0
    center: Vec2 = new Vec2(0, 0)

    constructor(canvas: Canvas, fractal: Fractal) {
        this.canvas = canvas
        this.fractal = fractal
    }

    render() {
        const width = this.canvas.width
        const height = this.canvas.height
        
        for (let py = 0; py < height; py++) {
            for (let px = 0; px < width; px++) {
                // Convert pixel coordinates to fractal coordinates
                const x0 = (px - width / 2) / (0.5 * this.zoom * width) + this.center.x
                const y0 = (py - height / 2) / (0.5 * this.zoom * height) + this.center.y
                
                // Compute the fractal value
                const iterations = this.fractal.computePoint(x0, y0)
                
                // Get the color and set the pixel
                const color = this.fractal.getColor(iterations)
                this.canvas.setPixel(px, py, color)
            }
        }
        
        // Update the display
        this.canvas.update()
    }
    
    zoomIn(factor: number = 1.5) {
        this.zoom *= factor
    }
    
    zoomOut(factor: number = 1.5) {
        this.zoom /= factor
    }
    
    move(dx: number, dy: number) {
        this.center.x += dx / this.zoom
        this.center.y += dy / this.zoom
    }
}

// Main application
function main() {
    // Create a canvas
    const canvas = new Canvas(800, 600, 'fractalCanvas')
    
    // Create a fractal
    const mandelbrot = new Mandelbrot(100)
    
    // Create a renderer
    const renderer = new FractalRenderer(canvas, mandelbrot)
    
    // Initial render
    renderer.render()
    
    // Add event listeners for interactivity
    canvas.onClick((x, y) => {
        // Zoom in at the clicked point
        const dx = (x - canvas.width / 2) / (0.5 * renderer.zoom * canvas.width)
        const dy = (y - canvas.height / 2) / (0.5 * renderer.zoom * canvas.height)
        renderer.center.x += dx
        renderer.center.y += dy
        renderer.zoomIn()
        renderer.render()
    })
    
    // Keyboard controls
    document.addEventListener('keydown', (event) => {
        const moveStep = 0.1 / renderer.zoom
        
        switch (event.key) {
            case 'ArrowUp':
                renderer.move(0, -moveStep)
                break
            case 'ArrowDown':
                renderer.move(0, moveStep)
                break
            case 'ArrowLeft':
                renderer.move(-moveStep, 0)
                break
            case 'ArrowRight':
                renderer.move(moveStep, 0)
                break
            case '+':
                renderer.zoomIn()
                break
            case '-':
                renderer.zoomOut()
                break
            case 'r':
                // Reset view
                renderer.zoom = 1.0
                renderer.center = new Vec2(0, 0)
                break
        }
        
        renderer.render()
    })
}

// Start the application
main()
