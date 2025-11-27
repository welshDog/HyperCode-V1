export * from './core/code-analyzer';
export * from './core/spatial-visualizer';

export interface VisualizationOptions {
  container: HTMLElement;
  code: string;
  language: string;
  onNodeClick?: (node: any) => void;
}

export class CodeVisualizer {
  private static instance: CodeVisualizer;
  private visualizer: any; // Reference to the spatial visualizer instance

  private constructor() {
    // Private constructor for singleton
  }

  public static getInstance(): CodeVisualizer {
    if (!CodeVisualizer.instance) {
      CodeVisualizer.instance = new CodeVisualizer();
    }
    return CodeVisualizer.instance;
  }

  public async visualize(options: VisualizationOptions): Promise<void> {
    const { codeAnalyzer, spatialVisualizer } = await import('./core');
    
    // Analyze the code
    const analysis = await codeAnalyzer.analyze(options.code, options.language);
    
    // Generate visualization
    const svgElement = spatialVisualizer.generateVisualization(analysis);
    
    // Clear container and append new visualization
    options.container.innerHTML = '';
    options.container.appendChild(svgElement);
  }

  public toggleVisualizationMode(): void {
    // Implementation to toggle between visualization modes
  }
}

// Export a singleton instance
export const codeVisualizer = CodeVisualizer.getInstance();
