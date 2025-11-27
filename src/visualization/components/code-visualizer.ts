import { codeVisualizer } from '..';

export class CodeVisualizerElement extends HTMLElement {
  private shadow: ShadowRoot;
  private container: HTMLElement;
  
  static get observedAttributes() {
    return ['code', 'language'];
  }

  constructor() {
    super();
    this.shadow = this.attachShadow({ mode: 'open' });
    this.container = document.createElement('div');
    this.container.style.width = '100%';
    this.container.style.height = '100%';
    this.shadow.appendChild(this.container);
  }

  connectedCallback() {
    this.render();
  }

  attributeChangedCallback(name: string, oldValue: string, newValue: string) {
    if (oldValue !== newValue) {
      this.render();
    }
  }

  private async render() {
    const code = this.getAttribute('code') || '';
    const language = this.getAttribute('language') || 'javascript';

    if (!code) return;

    try {
      await codeVisualizer.visualize({
        container: this.container,
        code,
        language,
        onNodeClick: (node) => {
          this.dispatchEvent(new CustomEvent('node-click', { 
            detail: { node } 
          }));
        }
      });
    } catch (error) {
      console.error('Error rendering code visualization:', error);
      this.container.innerHTML = `
        <div style="color: red; padding: 1rem;">
          Error rendering code visualization: ${error instanceof Error ? error.message : String(error)}
        </div>
      `;
    }
  }
}

// Register the custom element
if (!customElements.get('code-visualizer')) {
  customElements.define('code-visualizer', CodeVisualizerElement);
}

export default CodeVisualizerElement;
