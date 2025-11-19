"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.activate = activate;
exports.deactivate = deactivate;
const vscode = require("vscode");
function activate(context) {
    console.log("HyperCode Visual Syntax extension is now active!");
    // Register semantic annotation provider
    const provider = vscode.languages.registerCompletionItemProvider(["python", "hypercode"], {
        provideCompletionItems(document, position) {
            const annotations = [
                "?? @verifiable(...)",
                "?? @ensures(...)",
                "?? @requires(...)",
                "?? @intent(...)",
                "?? @accessibility(...)",
                "?? @computation(...)",
                "? @operation(...)",
                "?? @return(...)"
            ];
            return annotations.map(annotation => {
                const item = new vscode.CompletionItem(annotation, vscode.CompletionItemKind.Snippet);
                item.insertText = annotation;
                item.detail = "HyperCode semantic annotation";
                item.documentation = new vscode.MarkdownString(`Add ${annotation} semantic marker`);
                return item;
            });
        }
    }, "@");
    context.subscriptions.push(provider);
    // Register hover provider for semantic annotations
    const hoverProvider = vscode.languages.registerHoverProvider(["python", "hypercode"], {
        provideHover(document, position) {
            const line = document.lineAt(position.line);
            const text = line.text;
            // Check for semantic annotations
            const annotationMatch = text.match(/[???????????????]\s*@\w+/);
            if (annotationMatch) {
                const annotation = annotationMatch[0];
                const hoverInfo = getAnnotationHoverInfo(annotation);
                return new vscode.Hover(hoverInfo);
            }
            return null;
        }
    });
    context.subscriptions.push(hoverProvider);
}
function getAnnotationHoverInfo(annotation) {
    const info = {
        "?? @verifiable": "Verifiable - Formal verification and proof annotations",
        "?? @ensures": "Ensures - Postconditions and guarantees",
        "?? @requires": "Requires - Preconditions and dependencies",
        "?? @intent": "Intent - Purpose and cognitive context",
        "?? @accessibility": "Accessibility - Neurodiversity and inclusive design",
        "?? @computation": "Computation - Computational complexity and behavior",
        "? @operation": "Operation - Runtime operations and side effects",
        "?? @return": "Return - Return value specifications"
    };
    const description = info[annotation] || "Unknown semantic annotation";
    const markdown = new vscode.MarkdownString();
    markdown.appendMarkdown(`## ${annotation}\n\n`);
    markdown.appendMarkdown(`${description}\n\n`);
    markdown.appendMarkdown("*HyperCode Visual Semantic Syntax*");
    return markdown;
}
function deactivate() { }
//# sourceMappingURL=extension.js.map