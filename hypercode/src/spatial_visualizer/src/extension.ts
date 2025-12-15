import * as vscode from 'vscode';
import { SpatialVisualizer } from './spatial-visualizer';
import { CodeAnalyzer } from './code-analyzer';
import { VisualizationPanel } from './visualization-panel';

let visualizer: SpatialVisualizer;
let analyzer: CodeAnalyzer;

export async function activate(context: vscode.ExtensionContext) {
  console.log('🚀 Spatial Code Visualizer activated');

  // Initialize core components
  visualizer = new SpatialVisualizer();
  analyzer = new CodeAnalyzer();

  // Register command: Open Spatial Visualizer
  let openCommand = vscode.commands.registerCommand(
    'spatialVisualizer.open',
    async () => {
      const editor = vscode.window.activeTextEditor;
      if (!editor) {
        vscode.window.showWarningMessage('No active editor. Open a file first.');
        return;
      }

      try {
        // Analyze current file
        const filePath = editor.document.uri.fsPath;
        const codeContent = editor.document.getText();

        const analysis = await analyzer.analyze(codeContent, editor.document.languageId);

        // Create visualization panel
        const panel = new VisualizationPanel(
          context.extensionUri,
          filePath,
          analysis,
          visualizer
        );

        panel.show();
        vscode.window.showInformationMessage('✅ Spatial visualizer opened');
      } catch (error) {
        vscode.window.showErrorMessage(`Error: ${error instanceof Error ? error.message : 'Unknown error'}`);
      }
    }
  );

  // Register command: Toggle visualization mode
  let toggleCommand = vscode.commands.registerCommand(
    'spatialVisualizer.toggleMode',
    () => {
      visualizer.toggleMode();
      vscode.window.showInformationMessage(`📊 Visualization mode toggled`);
    }
  );

  // Listen for file changes
  const fileWatcher = vscode.workspace.onDidChangeTextDocument((event) => {
    if (event.document === vscode.window.activeTextEditor?.document) {
      // Trigger re-analysis on file change (debounced)
      visualizer.updateOnChange();
    }
  });

  context.subscriptions.push(openCommand, toggleCommand, fileWatcher);
}

export function deactivate() {
  console.log('🛑 Spatial Code Visualizer deactivated');
}
