import * as vscode from 'vscode';
import { CodeAnalysis } from './code-analyzer';
import { SpatialVisualizer } from './spatial-visualizer';

export class VisualizationPanel {
  private panel: vscode.WebviewPanel;
  private visualizer: SpatialVisualizer;
  private analysis: CodeAnalysis;

  constructor(
    extensionUri: vscode.Uri,
    private filePath: string,
    analysis: CodeAnalysis,
    visualizer: SpatialVisualizer
  ) {
    this.analysis = analysis;
    this.visualizer = visualizer;

    this.panel = vscode.window.createWebviewPanel(
      'spatialVisualizer',
      `🧠 Spatial View: ${filePath.split('/').pop()}`,
      vscode.ViewColumn.Beside,
      {
        enableScripts: true,
        localResourceRoots: [extensionUri]
      }
    );

    this.panel.webview.html = this.getWebviewContent();
  }

  show() {
    this.panel.reveal();
  }

  private getWebviewContent(): string {
    const analysis = this.analysis;

    // Build HTML with embedded SVG and interactive controls
    return `
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Spatial Code Visualizer</title>
        <script src="https://d3js.org/d3.v7.min.js"></script>
        <style>
          * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
          }

          body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
            background: #f9fafb;
            padding: 16px;
          }

          .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
            overflow: hidden;
          }

          .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
          }

          .header h1 {
            font-size: 20px;
            font-weight: 600;
          }

          .controls {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
          }

          button {
            background: rgba(255,255,255,0.2);
            border: 1px solid rgba(255,255,255,0.3);
            color: white;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 12px;
            font-weight: 500;
            transition: all 0.2s;
          }

          button:hover {
            background: rgba(255,255,255,0.3);
            transform: translateY(-1px);
          }

          .visualization {
            padding: 20px;
            background: white;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 600px;
          }

          svg {
            max-width: 100%;
            height: auto;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            background: white;
          }

          .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            padding: 20px;
            background: #f3f4f6;
            border-top: 1px solid #e5e7eb;
          }

          .stat-card {
            background: white;
            padding: 16px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
          }

          .stat-label {
            font-size: 12px;
            color: #6b7280;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
          }

          .stat-value {
            font-size: 24px;
            font-weight: 700;
            color: #111827;
            margin-top: 8px;
          }

          .nodes-list {
            padding: 20px;
            max-height: 300px;
            overflow-y: auto;
            border-top: 1px solid #e5e7eb;
          }

          .nodes-list h3 {
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 12px;
            color: #374151;
          }

          .node-item {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 8px;
            margin-bottom: 8px;
            background: #f9fafb;
            border-radius: 6px;
            font-size: 12px;
          }

          .node-badge {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
          }

          .accessibility-note {
            background: #fef3c7;
            border-left: 4px solid #f59e0b;
            padding: 12px;
            margin: 16px;
            border-radius: 6px;
            font-size: 12px;
            color: #92400e;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="header">
            <div>
              <h1>🧠 Spatial Code Visualizer</h1>
              <p style="font-size: 12px; opacity: 0.9; margin-top: 4px;">Neurodivergent-friendly code navigation</p>
            </div>
            <div class="controls">
              <button onclick="toggleMode()">📊 Switch Mode</button>
              <button onclick="toggleContrast()">⚙️ Toggle Contrast</button>
              <button onclick="exportSVG()">💾 Export</button>
            </div>
          </div>

          <div class="visualization" id="visualization">
            <svg viewBox="0 0 1200 800" width="1200" height="800"></svg>
          </div>

          <div class="stats">
            <div class="stat-card">
              <div class="stat-label">Cognitive Load</div>
              <div class="stat-value">${analysis.cognitiveLoadScore.toFixed(1)}/10</div>
            </div>
            <div class="stat-card">
              <div class="stat-label">Total Complexity</div>
              <div class="stat-value">${analysis.totalComplexity}</div>
            </div>
            <div class="stat-card">
              <div class="stat-label">Code Elements</div>
              <div class="stat-value">${analysis.nodes.length}</div>
            </div>
            <div class="stat-card">
              <div class="stat-label">Language</div>
              <div class="stat-value">${analysis.language.toUpperCase()}</div>
            </div>
          </div>

          <div class="nodes-list">
            <h3>📍 Code Elements (${analysis.nodes.length})</h3>
            ${analysis.nodes.map(node => \`
              <div class="node-item">
                <span class="node-badge" style="background: \${getColorForType('\${node.type}')}"></span>
                <strong>\${node.name}</strong>
                <span style="color: #9ca3af; margin-left: auto;">Line \${node.line}</span>
              </div>
            \`).join('')}
          </div>

          <div class="accessibility-note">
            💡 <strong>Accessibility Tip:</strong> This visualization is designed for ADHD/neurodivergent brains.
            Use the "Switch Mode" button to find your preferred layout. High cognitive load scores indicate areas
            that might benefit from refactoring.
          </div>
        </div>

        <script>
          function getColorForType(type) {
            const colors = {
              'function': '#6366f1',
              'class': '#ec4899',
              'variable': '#10b981',
              'import': '#f59e0b',
              'interface': '#8b5cf6'
            };
            return colors[type] || '#d1d5db';
          }

          function toggleMode() {
            alert('Mode switching activated! (Implementation connects to your IDE backend)');
          }

          function toggleContrast() {
            document.body.style.filter = document.body.style.filter === 'contrast(1.2)' ? 'contrast(1)' : 'contrast(1.2)';
          }

          function exportSVG() {
            const svg = document.querySelector('svg');
            const serializer = new XMLSerializer();
            const svgString = serializer.serializeToString(svg);
            const blob = new Blob([svgString], { type: 'image/svg+xml' });
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'code-visualization.svg';
            link.click();
          }

          // D3 rendering would happen here in production
          console.log('✅ Spatial Visualizer loaded');
        </script>
      </body>
      </html>
    `;
  }
}
