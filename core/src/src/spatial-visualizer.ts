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
    function: '#6366f1',      // indigo
    class: '#ec4899',          // pink
    variable: '#10b981',       // emerald
    import: '#f59e0b',         // amber
    interface: '#8b5cf6',      // violet
    link: '#d1d5db',           // gray
    background: '#ffffff',
    text: '#111827'
  };

  /**
   * Generate SVG visualization from code analysis
   */
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

  private renderMindMap(svg: d3.Selection<SVGSVGElement, unknown, HTMLElement, unknown>, analysis: CodeAnalysis) {
    const nodeRadius = 30;
    const width = 1200;
    const height = 800;

    // Center node (file/module)
    svg.append('circle')
      .attr('cx', width / 2)
      .attr('cy', height / 2)
      .attr('r', nodeRadius + 10)
      .attr('fill', '#fbbf24')
      .attr('opacity', 0.9);

    svg.append('text')
      .attr('x', width / 2)
      .attr('y', height / 2)
      .attr('text-anchor', 'middle')
      .attr('dy', '0.3em')
      .attr('font-size', '12px')
      .attr('font-weight', 'bold')
      .attr('fill', '#000')
      .text('Code');

    // Arrange nodes in concentric circles
    const nodesByType = this.groupNodesByType(analysis.nodes);
    let angleOffset = 0;
    let radiusOffset = 150;

    Object.entries(nodesByType).forEach(([type, nodes]) => {
      const angleStep = (Math.PI * 2) / nodes.length;

      nodes.forEach((node, idx) => {
        const angle = angleOffset + idx * angleStep;
        const x = width / 2 + radiusOffset * Math.cos(angle);
        const y = height / 2 + radiusOffset * Math.sin(angle);

        // Draw edge from center
        svg.append('line')
          .attr('x1', width / 2)
          .attr('y1', height / 2)
          .attr('x2', x)
          .attr('y2', y)
          .attr('stroke', this.colorScheme.link)
          .attr('stroke-width', 2)
          .attr('opacity', 0.5);

        // Draw node
        svg.append('circle')
          .attr('cx', x)
          .attr('cy', y)
          .attr('r', nodeRadius)
          .attr('fill', this.colorScheme[node.type as keyof typeof this.colorScheme])
          .attr('opacity', 0.8)
          .attr('cursor', 'pointer');

        // Node label
        svg.append('text')
          .attr('x', x)
          .attr('y', y)
          .attr('text-anchor', 'middle')
          .attr('dy', '0.3em')
          .attr('font-size', '10px')
          .attr('font-weight', 'bold')
          .attr('fill', '#fff')
          .text(node.name.substring(0, 8))
          .attr('pointer-events', 'none');

        // Cognitive load indicator (ring)
        const ringOpacity = node.cognitiveLoad / 10;
        svg.append('circle')
          .attr('cx', x)
          .attr('cy', y)
          .attr('r', nodeRadius + 5)
          .attr('fill', 'none')
          .attr('stroke', '#ef4444')
          .attr('stroke-width', 2)
          .attr('opacity', ringOpacity);
      });

      radiusOffset += 100;
    });

    // Add cognitive load legend
    this.addLegend(svg, analysis);
  }

  private renderForceDirected(svg: d3.Selection<SVGSVGElement, unknown, HTMLElement, unknown>, analysis: CodeAnalysis) {
    const width = 1200;
    const height = 800;

    const simulation = d3.forceSimulation(analysis.nodes)
      .force('link', d3.forceLink<CodeNode, any>()
        .id((d: CodeNode) => d.name)
        .distance(100))
      .force('charge', d3.forceManyBody().strength(-300))
      .force('center', d3.forceCenter(width / 2, height / 2))
      .force('collision', d3.forceCollide(40));

    // Render links
    svg.selectAll('line')
      .data(analysis.relationships)
      .enter()
      .append('line')
      .attr('stroke', this.colorScheme.link)
      .attr('stroke-width', 2)
      .attr('opacity', 0.5);

    // Render nodes
    const nodes = svg.selectAll('circle')
      .data(analysis.nodes)
      .enter()
      .append('circle')
      .attr('r', (d: CodeNode) => 30 + d.complexity * 5)
      .attr('fill', (d: CodeNode) => this.colorScheme[d.type as keyof typeof this.colorScheme])
      .attr('opacity', 0.8);

    // Labels
    svg.selectAll('text')
      .data(analysis.nodes)
      .enter()
      .append('text')
      .attr('text-anchor', 'middle')
      .attr('dy', '0.3em')
      .attr('font-size', '10px')
      .attr('fill', '#fff')
      .text((d: CodeNode) => d.name.substring(0, 10));

    simulation.on('tick', () => {
      nodes.attr('cx', (d: any) => d.x).attr('cy', (d: any) => d.y);
    });
  }

  private renderHierarchical(svg: d3.Selection<SVGSVGElement, unknown, HTMLElement, unknown>, analysis: CodeAnalysis) {
    const width = 1200;
    const height = 800;
    const depth = 3;

    const nodesByDepth: CodeNode[][] = [[], [], []];
    analysis.nodes.forEach((node, idx) => {
      nodesByDepth[idx % depth].push(node);
    });

    nodesByDepth.forEach((nodesAtDepth, depthIdx) => {
      const xSpacing = width / (nodesAtDepth.length + 1);
      const y = 100 + depthIdx * 300;

      nodesAtDepth.forEach((node, idx) => {
        const x = xSpacing * (idx + 1);

        svg.append('circle')
          .attr('cx', x)
          .attr('cy', y)
          .attr('r', 30)
          .attr('fill', this.colorScheme[node.type as keyof typeof this.colorScheme])
          .attr('opacity', 0.8);

        svg.append('text')
          .attr('x', x)
          .attr('y', y)
          .attr('text-anchor', 'middle')
          .attr('dy', '0.3em')
          .attr('font-size', '10px')
          .attr('fill', '#fff')
          .text(node.name.substring(0, 8));
      });
    });

    this.addLegend(svg, analysis);
  }

  private renderRadial(svg: d3.Selection<SVGSVGElement, unknown, HTMLElement, unknown>, analysis: CodeAnalysis) {
    const width = 1200;
    const height = 800;
    const centerX = width / 2;
    const centerY = height / 2;

    const angleStep = (Math.PI * 2) / analysis.nodes.length;
    const radius = 300;

    analysis.nodes.forEach((node, idx) => {
      const angle = idx * angleStep;
      const x = centerX + radius * Math.cos(angle);
      const y = centerY + radius * Math.sin(angle);

      svg.append('line')
        .attr('x1', centerX)
        .attr('y1', centerY)
        .attr('x2', x)
        .attr('y2', y)
        .attr('stroke', this.colorScheme.link)
        .attr('stroke-width', 1)
        .attr('opacity', 0.3);

      svg.append('circle')
        .attr('cx', x)
        .attr('cy', y)
        .attr('r', 30)
        .attr('fill', this.colorScheme[node.type as keyof typeof this.colorScheme])
        .attr('opacity', 0.8);

      svg.append('text')
        .attr('x', x)
        .attr('y', y)
        .attr('text-anchor', 'middle')
        .attr('dy', '0.3em')
        .attr('font-size', '10px')
        .attr('fill', '#fff')
        .text(node.name.substring(0, 8));
    });

    this.addLegend(svg, analysis);
  }

  private groupNodesByType(nodes: CodeNode[]): Record<string, CodeNode[]> {
    return nodes.reduce((acc, node) => {
      if (!acc[node.type]) acc[node.type] = [];
      acc[node.type].push(node);
      return acc;
    }, {} as Record<string, CodeNode[]>);
  }

  private addLegend(svg: d3.Selection<SVGSVGElement, unknown, HTMLElement, unknown>, analysis: CodeAnalysis) {
    const legendX = 20;
    const legendY = 20;
    const itemHeight = 25;

    svg.append('text')
      .attr('x', legendX)
      .attr('y', legendY)
      .attr('font-size', '12px')
      .attr('font-weight', 'bold')
      .text(`Cognitive Load: ${analysis.cognitiveLoadScore.toFixed(1)}/10`);

    Object.entries(this.colorScheme).slice(0, 5).forEach(([type, color], idx) => {
      if (type === 'function' || type === 'class' || type === 'variable') {
        svg.append('circle')
          .attr('cx', legendX + 10)
          .attr('cy', legendY + 30 + idx * itemHeight)
          .attr('r', 6)
          .attr('fill', color);

        svg.append('text')
          .attr('x', legendX + 25)
          .attr('y', legendY + 35 + idx * itemHeight)
          .attr('font-size', '11px')
          .text(type);
      }
    });
  }

  toggleMode() {
    const modes: VisualizationMode['type'][] = ['mindmap', 'force-directed', 'hierarchical', 'radial'];
    const currentIdx = modes.indexOf(this.mode.type);
    this.mode.type = modes[(currentIdx + 1) % modes.length];
  }

  updateOnChange() {
    // Debounced re-render trigger
    console.log('📊 Code changed, visualization will update');
  }
}
