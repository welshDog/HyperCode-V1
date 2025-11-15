import * as parser from 'typescript-ast-parser';

export interface CodeNode {
  name: string;
  type: 'function' | 'class' | 'variable' | 'import' | 'interface';
  line: number;
  complexity: number;
  cognitiveLoad: number;
  dependencies: string[];
  description?: string;
}

export interface CodeAnalysis {
  nodes: CodeNode[];
  relationships: Array<{ from: string; to: string; type: string }>;
  cognitiveLoadScore: number;
  language: string;
  totalComplexity: number;
}

export class CodeAnalyzer {
  /**
   * Analyzes code structure and relationships
   * Returns spatial metadata for mind-map visualization
   */
  async analyze(code: string, language: string): Promise<CodeAnalysis> {
    const nodes: CodeNode[] = [];
    const relationships: Array<{ from: string; to: string; type: string }> = [];

    try {
      // Parse based on language
      if (language === 'python' || language === 'py') {
        return this.analyzePython(code);
      } else if (language === 'javascript' || language === 'typescript') {
        return this.analyzeJavaScript(code);
      } else {
        return this.analyzeGeneric(code);
      }
    } catch (error) {
      console.error('Analysis error:', error);
      return {
        nodes: [],
        relationships: [],
        cognitiveLoadScore: 0,
        language,
        totalComplexity: 0
      };
    }
  }

  private analyzePython(code: string): CodeAnalysis {
    const nodes: CodeNode[] = [];
    const lines = code.split('\n');
    const relationships: Array<{ from: string; to: string; type: string }> = [];

    lines.forEach((line, idx) => {
      const trimmed = line.trim();

      // Detect functions
      if (trimmed.startsWith('def ')) {
        const match = trimmed.match(/def\s+(\w+)\s*\(/);
        if (match) {
          nodes.push({
            name: match[1],
            type: 'function',
            line: idx + 1,
            complexity: this.calculateComplexity(code, match[1]),
            cognitiveLoad: this.calculateCognitiveLoad(line),
            dependencies: this.extractDependencies(code, match[1])
          });
        }
      }

      // Detect classes
      if (trimmed.startsWith('class ')) {
        const match = trimmed.match(/class\s+(\w+)/);
        if (match) {
          nodes.push({
            name: match[1],
            type: 'class',
            line: idx + 1,
            complexity: 0,
            cognitiveLoad: this.calculateCognitiveLoad(line),
            dependencies: []
          });
        }
      }

      // Detect imports
      if (trimmed.startsWith('import ') || trimmed.startsWith('from ')) {
        nodes.push({
          name: trimmed,
          type: 'import',
          line: idx + 1,
          complexity: 0,
          cognitiveLoad: 1,
          dependencies: []
        });
      }
    });

    const cognitiveLoadScore = nodes.reduce((sum, n) => sum + n.cognitiveLoad, 0) / Math.max(nodes.length, 1);
    const totalComplexity = nodes.reduce((sum, n) => sum + n.complexity, 0);

    return {
      nodes,
      relationships,
      cognitiveLoadScore,
      language: 'python',
      totalComplexity
    };
  }

  private analyzeJavaScript(code: string): CodeAnalysis {
    const nodes: CodeNode[] = [];
    const lines = code.split('\n');

    lines.forEach((line, idx) => {
      const trimmed = line.trim();

      // Detect functions
      if (trimmed.match(/function\s+\w+|const\s+\w+\s*=\s*(async\s*)?\(/)) {
        const match = trimmed.match(/(?:function\s+|const\s+)(\w+)/);
        if (match) {
          nodes.push({
            name: match[1],
            type: 'function',
            line: idx + 1,
            complexity: this.calculateComplexity(code, match[1]),
            cognitiveLoad: this.calculateCognitiveLoad(line),
            dependencies: []
          });
        }
      }

      // Detect classes
      if (trimmed.startsWith('class ')) {
        const match = trimmed.match(/class\s+(\w+)/);
        if (match) {
          nodes.push({
            name: match[1],
            type: 'class',
            line: idx + 1,
            complexity: 0,
            cognitiveLoad: this.calculateCognitiveLoad(line),
            dependencies: []
          });
        }
      }

      // Detect imports
      if (trimmed.startsWith('import ') || trimmed.startsWith('require(')) {
        nodes.push({
          name: trimmed,
          type: 'import',
          line: idx + 1,
          complexity: 0,
          cognitiveLoad: 1,
          dependencies: []
        });
      }
    });

    const cognitiveLoadScore = nodes.reduce((sum, n) => sum + n.cognitiveLoad, 0) / Math.max(nodes.length, 1);
    const totalComplexity = nodes.reduce((sum, n) => sum + n.complexity, 0);

    return {
      nodes,
      relationships: [],
      cognitiveLoadScore,
      language: 'javascript',
      totalComplexity
    };
  }

  private analyzeGeneric(code: string): CodeAnalysis {
    const nodes: CodeNode[] = [];
    const lines = code.split('\n');

    lines.forEach((line, idx) => {
      if (line.trim().length > 0) {
        nodes.push({
          name: line.trim().substring(0, 50),
          type: 'variable',
          line: idx + 1,
          complexity: 0,
          cognitiveLoad: 1,
          dependencies: []
        });
      }
    });

    return {
      nodes: nodes.slice(0, 20),
      relationships: [],
      cognitiveLoadScore: 1,
      language: 'unknown',
      totalComplexity: 0
    };
  }

  private calculateComplexity(code: string, funcName: string): number {
    // Simplified cyclomatic complexity estimation
    const funcStart = code.indexOf(funcName);
    if (funcStart === -1) return 1;

    const funcEnd = code.indexOf('\n\n', funcStart) || code.length;
    const funcCode = code.substring(funcStart, funcEnd);

    const ifCount = (funcCode.match(/\bif\b/g) || []).length;
    const forCount = (funcCode.match(/\bfor\b/g) || []).length;
    const whileCount = (funcCode.match(/\bwhile\b/g) || []).length;
    const caseCount = (funcCode.match(/\bcase\b/g) || []).length;

    return 1 + ifCount + forCount + whileCount + caseCount;
  }

  private calculateCognitiveLoad(line: string): number {
    let load = 1;
    load += (line.match(/\(/g) || []).length * 0.2;
    load += (line.match(/\{/g) || []).length * 0.2;
    load += (line.length > 80) ? 0.5 : 0;
    return Math.min(load, 10);
  }

  private extractDependencies(code: string, funcName: string): string[] {
    const deps: string[] = [];
    const funcStart = code.indexOf(`function ${funcName}`) || code.indexOf(`def ${funcName}`);
    if (funcStart === -1) return deps;

    const funcEnd = code.indexOf('\n\n', funcStart) || code.length;
    const funcCode = code.substring(funcStart, funcEnd);

    const callMatches = funcCode.matchAll(/(\w+)\s*\(/g);
    for (const match of callMatches) {
      if (match[1] !== funcName && !['if', 'for', 'while', 'return'].includes(match[1])) {
        deps.push(match[1]);
      }
    }

    return [...new Set(deps)];
  }
}
