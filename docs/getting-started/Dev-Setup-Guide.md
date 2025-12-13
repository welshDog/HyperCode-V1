# HC-001 Developer Setup Guide

## 🎯 Your Mission (Developer Role)

You're building the **React + reactflow canvas** for the HyperCode Visual Programming Interface.

**What you'll ship in 8 weeks:**
- ✅ Canvas component (drag-drop nodes, connections)
- ✅ 12 core node types (rendered, configurable)
- ✅ Node palette (searchable, categorized)
- ✅ Properties panel (node configuration)
- ✅ Code generator (visual → HyperCode text)
- ✅ Undo/redo system
- ✅ Save/load (JSON persistence)
- ✅ Keyboard shortcuts
- ✅ Accessibility (WCAG 2.1 AA)

---

## 📋 Week 1: Setup & Scaffold (Dec 2-8)

### Phase 1.1: Project Init (Day 1-2)

**Create React project:**
```bash
# Option A: Vite (faster, modern)
npm create vite@latest hypercode-visual -- --template react-ts
cd hypercode-visual
npm install

# Option B: Create React App (familiar)
npx create-react-app hypercode-visual --template typescript
cd hypercode-visual
```

**Install core dependencies:**
```bash
npm install reactflow typescript axios zustand react-icons
npm install -D tailwindcss postcss autoprefixer vitest @testing-library/react
npx tailwindcss init -p
```

**Why these?**
- **reactflow**: Battle-tested node editor library
- **zustand**: Lightweight state management (better than Redux for this)
- **react-icons**: Icon library (easy accessibility)
- **tailwindcss**: CSS-in-utility (accessible, fast)
- **vitest**: Modern testing framework

### Phase 1.2: Project Structure (Day 2-3)

```
hypercode-visual/
├── src/
│   ├── components/
│   │   ├── Canvas/
│   │   │   ├── Canvas.tsx         # Main editor container
│   │   │   ├── useNodeGraph.ts    # State management hook
│   │   │   └── Canvas.module.css
│   │   ├── Node/
│   │   │   ├── Node.tsx           # Custom node component
│   │   │   ├── NodeTypes.ts       # Node type definitions
│   │   │   └── nodes/             # Individual node implementations
│   │   ├── Palette/
│   │   │   ├── Palette.tsx        # Left sidebar node list
│   │   │   └── Palette.module.css
│   │   ├── PropertiesPanel/
│   │   │   ├── PropertiesPanel.tsx
│   │   │   └── PropertiesPanel.module.css
│   │   ├── CodeOutput/
│   │   │   ├── CodeOutput.tsx     # Live code display
│   │   │   └── CodeGenerator.ts   # Visual → Text conversion
│   │   └── Toolbar/
│   │       ├── Toolbar.tsx
│   │       └── Toolbar.module.css
│   ├── hooks/
│   │   ├── useUndoRedo.ts
│   │   ├── useKeyboardShortcuts.ts
│   │   ├── useNodeValidation.ts
│   │   └── useLocalStorage.ts
│   ├── utils/
│   │   ├── nodeSchema.ts          # Node type definitions
│   │   ├── validation.ts          # Type checking
│   │   ├── codeGenerator.ts       # Convert graph to code
│   │   ├── codeParser.ts          # Parse code to graph (future)
│   │   └── constants.ts
│   ├── types/
│   │   ├── nodes.ts               # TypeScript interfaces
│   │   ├── edges.ts
│   │   └── index.ts
│   ├── styles/
│   │   ├── tokens.css             # Design system
│   │   ├── accessibility.css      # A11y overrides
│   │   └── globals.css
│   ├── App.tsx
│   └── main.tsx
├── tests/
│   ├── nodeSchema.test.ts
│   ├── codeGenerator.test.ts
│   ├── Canvas.test.tsx
│   └── nodeValidation.test.ts
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CONTRIBUTING.md
│   └── ACCESSIBILITY.md
├── .github/
│   └── workflows/
│       ├── test.yml
│       ├── accessibility-check.yml
│       └── build.yml
├── tsconfig.json
├── vite.config.ts
├── package.json
└── README.md
```

### Phase 1.3: TypeScript Types (Day 3-4)

**File: `src/types/nodes.ts`**

```typescript
// Node type definitions
export type NodeType = 
  | 'input' 
  | 'output' 
  | 'parse' 
  | 'filter' 
  | 'map' 
  | 'loop' 
  | 'if-else' 
  | 'try-catch'
  | 'ai-gpt'
  | 'ai-claude'
  | 'variable'
  | 'custom';

export interface NodeData {
  id: string;
  type: NodeType;
  label: string;
  config: Record<string, any>;
  inputs: PortDefinition[];
  outputs: PortDefinition[];
}

export interface PortDefinition {
  id: string;
  name: string;
  type: 'string' | 'number' | 'boolean' | 'array' | 'object' | 'any';
  required: boolean;
  defaultValue?: any;
}

export interface HyperCodeEdge {
  id: string;
  source: string;
  target: string;
  sourceHandle: string;
  targetHandle: string;
  type: 'data' | 'control';
}

export interface NodeGraph {
  nodes: NodeData[];
  edges: HyperCodeEdge[];
  metadata: {
    name: string;
    description: string;
    createdAt: string;
    updatedAt: string;
  };
}
```

### Phase 1.4: Node Schema (Day 4-5)

**File: `src/utils/nodeSchema.ts`**

```typescript
import { NodeType, NodeData, PortDefinition } from '../types/nodes';

export const NODE_CATEGORIES = {
  INPUT_OUTPUT: 'Input/Output',
  TRANSFORM: 'Transform',
  CONTROL_FLOW: 'Control Flow',
  AI_INTEGRATION: 'AI Integration',
  STATE: 'State Management',
  CUSTOM: 'Custom',
} as const;

export const NODE_COLORS = {
  INPUT_OUTPUT: '#3b82f6',    // Blue
  TRANSFORM: '#10b981',       // Green
  CONTROL_FLOW: '#f59e0b',    // Orange
  AI_INTEGRATION: '#a855f7',  // Purple
  STATE: '#6366f1',           // Indigo
  CUSTOM: '#64748b',          // Gray
} as const;

export const NODE_DEFINITIONS: Record<NodeType, {
  label: string;
  category: string;
  color: string;
  description: string;
  inputs: PortDefinition[];
  outputs: PortDefinition[];
}> = {
  input: {
    label: 'Input',
    category: NODE_CATEGORIES.INPUT_OUTPUT,
    color: NODE_COLORS.INPUT_OUTPUT,
    description: 'Read data from file, API, or user',
    inputs: [],
    outputs: [
      { id: 'out_data', name: 'data', type: 'any', required: true }
    ],
  },
  output: {
    label: 'Output',
    category: NODE_CATEGORIES.INPUT_OUTPUT,
    color: NODE_COLORS.INPUT_OUTPUT,
    description: 'Send data to file, API, or display',
    inputs: [
      { id: 'in_data', name: 'data', type: 'any', required: true }
    ],
    outputs: [],
  },
  parse: {
    label: 'Parse',
    category: NODE_CATEGORIES.TRANSFORM,
    color: NODE_COLORS.TRANSFORM,
    description: 'Parse JSON, CSV, or other formats',
    inputs: [
      { id: 'in_raw', name: 'raw', type: 'string', required: true }
    ],
    outputs: [
      { id: 'out_parsed', name: 'parsed', type: 'object', required: true }
    ],
  },
  filter: {
    label: 'Filter',
    category: NODE_CATEGORIES.TRANSFORM,
    color: NODE_COLORS.TRANSFORM,
    description: 'Filter array by condition',
    inputs: [
      { id: 'in_array', name: 'array', type: 'array', required: true },
      { id: 'in_condition', name: 'condition', type: 'any', required: true }
    ],
    outputs: [
      { id: 'out_filtered', name: 'filtered', type: 'array', required: true }
    ],
  },
  // ... more node types
  loop: {
    label: 'Loop',
    category: NODE_CATEGORIES.CONTROL_FLOW,
    color: NODE_COLORS.CONTROL_FLOW,
    description: 'Iterate over array',
    inputs: [
      { id: 'in_array', name: 'array', type: 'array', required: true }
    ],
    outputs: [
      { id: 'out_item', name: 'item', type: 'any', required: true },
      { id: 'out_index', name: 'index', type: 'number', required: true }
    ],
  },
  'ai-gpt': {
    label: 'Ask GPT',
    category: NODE_CATEGORIES.AI_INTEGRATION,
    color: NODE_COLORS.AI_INTEGRATION,
    description: 'Ask GPT-4 a question',
    inputs: [
      { id: 'in_prompt', name: 'prompt', type: 'string', required: true },
      { id: 'in_context', name: 'context', type: 'any', required: false }
    ],
    outputs: [
      { id: 'out_response', name: 'response', type: 'string', required: true }
    ],
  },
  // ... rest of node types
};
```

### Phase 1.5: Zustand State (Day 5)

**File: `src/components/Canvas/useNodeGraph.ts`**

```typescript
import { create } from 'zustand';
import { NodeData, HyperCodeEdge, NodeGraph } from '../../types/nodes';

interface NodeGraphState {
  nodes: NodeData[];
  edges: HyperCodeEdge[];
  selectedNodeId: string | null;
  
  // Actions
  addNode: (node: NodeData) => void;
  removeNode: (nodeId: string) => void;
  updateNode: (nodeId: string, data: Partial<NodeData>) => void;
  
  addEdge: (edge: HyperCodeEdge) => void;
  removeEdge: (edgeId: string) => void;
  
  selectNode: (nodeId: string | null) => void;
  
  clear: () => void;
  getGraph: () => NodeGraph;
  loadGraph: (graph: NodeGraph) => void;
}

export const useNodeGraph = create<NodeGraphState>((set, get) => ({
  nodes: [],
  edges: [],
  selectedNodeId: null,
  
  addNode: (node) => set((state) => ({
    nodes: [...state.nodes, node],
  })),
  
  removeNode: (nodeId) => set((state) => ({
    nodes: state.nodes.filter((n) => n.id !== nodeId),
    edges: state.edges.filter((e) => e.source !== nodeId && e.target !== nodeId),
  })),
  
  updateNode: (nodeId, data) => set((state) => ({
    nodes: state.nodes.map((n) => n.id === nodeId ? { ...n, ...data } : n),
  })),
  
  addEdge: (edge) => set((state) => ({
    edges: [...state.edges, edge],
  })),
  
  removeEdge: (edgeId) => set((state) => ({
    edges: state.edges.filter((e) => e.id !== edgeId),
  })),
  
  selectNode: (nodeId) => set({ selectedNodeId: nodeId }),
  
  clear: () => set({ nodes: [], edges: [], selectedNodeId: null }),
  
  getGraph: () => {
    const state = get();
    return {
      nodes: state.nodes,
      edges: state.edges,
      metadata: {
        name: 'HyperCode Program',
        description: '',
        createdAt: new Date().toISOString(),
        updatedAt: new Date().toISOString(),
      },
    };
  },
  
  loadGraph: (graph) => set({
    nodes: graph.nodes,
    edges: graph.edges,
  }),
}));
```

### Phase 1.6: Basic Canvas (Day 6-7)

**File: `src/components/Canvas/Canvas.tsx`**

```typescript
import React, { useCallback } from 'react';
import ReactFlow, {
  Node,
  Edge,
  addEdge,
  Connection,
  useNodesState,
  useEdgesState,
} from 'reactflow';
import 'reactflow/dist/style.css';
import { useNodeGraph } from './useNodeGraph';
import CustomNode from '../Node/Node';
import './Canvas.module.css';

const nodeTypes = { custom: CustomNode };

export default function Canvas() {
  const { nodes: graphNodes, edges: graphEdges, addEdge: addGraphEdge } = useNodeGraph();
  const [nodes, setNodes, onNodesChange] = useNodesState(
    graphNodes.map((n) => ({
      id: n.id,
      data: { label: n.label, ...n.config },
      position: { x: 0, y: 0 }, // Will be set by layout
      type: 'custom',
    }))
  );
  
  const [edges, setEdges, onEdgesChange] = useEdgesState(graphEdges);
  
  const onConnect = useCallback(
    (connection: Connection) => {
      const newEdge: Edge = {
        id: `${connection.source}-${connection.target}`,
        source: connection.source || '',
        target: connection.target || '',
        sourceHandle: connection.sourceHandle || '',
        targetHandle: connection.targetHandle || '',
      };
      setEdges((eds) => addEdge(connection, eds));
      addGraphEdge({
        ...newEdge,
        type: 'data',
      });
    },
    [setEdges, addGraphEdge]
  );
  
  return (
    <div className="canvas-container">
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        nodeTypes={nodeTypes}
        fitView
      >
        {/* Will add background, controls, etc. */}
      </ReactFlow>
    </div>
  );
}
```

---

## 📅 Week 2-3: Core Components (Dec 9-22)

### Build These Components:

1. **Custom Node Component** (Day 8-10)
   - Render node with inputs/outputs
   - Show node type icon + color
   - Accessible handles for connections
   - Hover tooltips

2. **Node Palette** (Day 11-12)
   - Categorized node list
   - Drag-drop to canvas
   - Search/filter
   - Icon + description for each

3. **Properties Panel** (Day 13-14)
   - Show selected node config
   - Input fields for properties
   - Type validation
   - Real-time preview

4. **Code Generator** (Day 15-18)
   - Walk the graph
   - Generate HyperCode text
   - Handle node order/dependencies
   - Format nicely

---

## 🧪 Week 4: Testing & Polish (Dec 23-29)

### Unit Tests
- Node schema validation
- Code generation correctness
- Graph operations (add, remove, connect)

### Integration Tests
- End-to-end workflow
- Save/load cycle
- Undo/redo reliability

### Accessibility Tests
- WCAG 2.1 AA compliance
- Keyboard navigation
- Screen reader support

---

## 🚀 Immediate Action Items (This Week)

**By Dec 5:**
1. [ ] Create React project
2. [ ] Install dependencies
3. [ ] Create project structure
4. [ ] Set up TypeScript types

**By Dec 8:**
1. [ ] Node schema defined
2. [ ] Zustand store set up
3. [ ] Basic Canvas rendering
4. [ ] Push to GitHub

---

## 💻 Commands You'll Use

```bash
# Start dev server
npm run dev

# Run tests
npm run test

# Build for production
npm run build

# Format code
npm run format

# Type check
npm run type-check
```

---

## 🔗 Key Resources

- **reactflow docs**: https://reactflow.dev
- **Zustand docs**: https://github.com/pmndrs/zustand
- **TypeScript handbook**: https://www.typescriptlang.org/docs/
- **Tailwind CSS**: https://tailwindcss.com/docs
- **Vitest**: https://vitest.dev

---

## 📊 Success Metrics (Week 1)

Done when:
- ✅ Project scaffolded
- ✅ All types defined
- ✅ Node schema complete
- ✅ Zustand store working
- ✅ Basic Canvas renders nodes
- ✅ Code pushed to GitHub

---

## 💬 Need Help?

- Discord: #hc-001-dev
- GitHub Issues: Label with `dev-help`
- Code reviews: Post PR for feedback

---

**Welcome to the dev team. Let's build something revolutionary.** 🚀

Now go pick a task and start coding! 💪