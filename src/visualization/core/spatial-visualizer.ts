import * as d3 from 'd3';
import { CodeAnalysis, CodeNode } from './code-analyzer';

export interface VisualizationMode {
  type: 'mindmap' | 'force-directed' | 'hierarchical' | 'radial';
  minimalNoise: boolean;
  highContrast: boolean;
}

export class SpatialVisualizer {
  private mode: VisualizationMode = {
    type: 'mindmap',
    minimalNoise: true,
    highContrast: false
  };

  private colorScheme = {
    function: '#6366f1',
    class: '#ec4899',
    variable: '#10b981',
    import: '#f59e0b',
    interface: '#8b5cf6',
    link: '#d1d5db',
    background: '#ffffff',
    text: '#111827'
  };

  generateVisualization(analysis: CodeAnalysis): SVGElement {
    const svg = d3.create('svg')
      .attr('viewBox', [0, 0, 1200, 800])
      .attr('style', 'max-width: 100%; height: auto; background: white;');

    if (this.mode.type === 'mindmap') {
      this.renderMindMap(svg, analysis);
    } else if (this.mode.type === 'force-directed') {
      this.renderForceDirected(svg, analysis);
    } else if (this.mode.type === 'hierarchical') {
      this.renderHierarchical(svg, analysis);
    } else if (this.mode.type === 'radial') {
      this.renderRadial(svg, analysis);
    }

    return svg.node() as SVGElement;
  }

  // ... (rest of the visualization methods)
  // [Previous implementation of renderMindMap, renderForceDirected, etc.]

  toggleMode() {
    const modes: VisualizationMode['type'][] = ['mindmap', 'force-directed', 'hierarchical', 'radial'];
    const currentIndex = modes.indexOf(this.mode.type);
    this.mode.type = modes[(currentIndex + 1) % modes.length];
  }

  setMode(mode: VisualizationMode['type']) {
    this.mode.type = mode;
  }
}

// Export a singleton instance
export const spatialVisualizer = new SpatialVisualizer();
