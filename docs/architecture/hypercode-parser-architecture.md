# HyperCode Parser Architecture

## Overview
The HyperCode parser module is a dual-stage system designed to bridge the gap between neurodivergent-friendly visual semantics and machine-executable logic. It consists of two primary components: the **Visual Syntax Parser** and the **Core AST Parser**.

## Pipeline Architecture

```mermaid
graph TD
    A[Raw HyperCode Source (.hc)] --> B[Visual Syntax Parser]
    B --> C{Semantic Extraction}
    C -- Metadata --> D[Neurodiversity Compliance Check]
    C -- Code Structure --> E[Lexer]
    E --> F[Token Stream]
    F --> G[HyperCodeParser (Core)]
    G --> H[Abstract Syntax Tree (AST)]
    H --> I[Runtime/Interpreter]
```

### 1. Visual Syntax Parser (`visual_syntax_parser.py`)
- **Role:** The "Frontend" of the parsing pipeline.
- **Responsibility:** Extracts semantic meaning from emoji markers (e.g., `🔍`, `🧠`) without affecting execution logic.
- **Output:** `ParsedFunction` objects with semantic annotations.
- **Key Feature:** Validates "Neurodiversity Compliance" (cognitive load, accessibility features).

### 2. Core Parser (`hypercode-parser-COMPLETE.py`)
- **Role:** The "Backend" parser.
- **Responsibility:** Converts the tokenized code into an Abstract Syntax Tree (AST) for execution.
- **Algorithm:** Recursive Descent.
- **Key Feature:** Supports loops, spatial 2D operations, and AI-native constructs.

## Key Algorithms & Complexity

### Semantic Pattern Matching
- **Implementation:** `VisualSyntaxParser._build_semantic_patterns`
- **Method:** Regex-based pattern matching for 13 distinct semantic markers.
- **Complexity:** **O(N * P)** where N is line count and P is number of patterns (constant).
- **Design Choice:** Regex allows flexible parameter parsing (e.g., `@ensures("x > 0")`) that would be complex for a standard tokenizer.

### Recursive Descent Parsing
- **Implementation:** `HyperCodeParser.parse`
- **Method:** Standard top-down recursive descent with single-token lookahead.
- **Complexity:** **O(N)** where N is number of tokens.
- **Design Choice:** chosen for readability and ease of debugging. It maps directly to the HyperCode grammar structure.

## Known Limitations & TODOs

### Limitations
1. **Operator Precedence:** The current `_parse_statement` dispatcher is flat. Complex mathematical expressions likely need a stronger precedence parser (e.g., Pratt Parser).
2. **Error Recovery:** The parser throws `ParserError` immediately. Better error recovery (synchronization points) would improve the IDE experience.
3. **Regex Brittleness:** `VisualSyntaxParser` relies on regex line-by-line. Multi-line annotations might break this.

### Future Improvements
- [ ] Implement Pratt parsing for expressions.
- [ ] Add support for "Panic Mode" error recovery.
- [ ] Integrate `VisualSyntaxParser` semantics directly into `ASTNode` metadata for runtime enforcement.
