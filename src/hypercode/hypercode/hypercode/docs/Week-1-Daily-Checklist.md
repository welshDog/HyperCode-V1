# HC-001 Developer - Week 1 Daily Checklist

## 🎯 Your Role
**React Developer building the Visual Programming Canvas**

**End Goal (Week 1)**: Working Canvas that renders nodes, with complete TypeScript types and Zustand state.

---

## ✅ Daily Tasks

### Monday, Dec 2 (TODAY)
**Focus**: Project setup & architecture planning

**Tasks:**
- [ ] Read Dev-Setup-Guide.md completely
- [ ] Choose your bundler: Vite or Create React App
- [ ] Create new project locally
- [ ] Install all dependencies (reactflow, zustand, etc.)
- [ ] Create folder structure as shown
- [ ] Push initial scaffold to GitHub

**Command:**
```bash
npm create vite@latest hypercode-visual -- --template react-ts
cd hypercode-visual
npm install reactflow zustand react-icons axios
npm install -D tailwindcss postcss autoprefixer vitest @testing-library/react
npx tailwindcss init -p
git init && git add . && git commit -m "Initial project scaffold"
```

**Done when**: 
- Project runs locally (`npm run dev`)
- Folder structure matches Dev-Setup-Guide.md
- GitHub repo created with initial commit

**Time estimate**: 2-3 hours

---

### Tuesday, Dec 3
**Focus**: TypeScript types & Node schema

**Tasks:**
- [ ] Create `src/types/nodes.ts` with all type definitions
- [ ] Create `src/utils/nodeSchema.ts` with 12 node definitions
- [ ] Create `src/utils/constants.ts` for colors, categories
- [ ] Write unit tests for node schema validation
- [ ] Document node schema in `docs/NODE_SCHEMA.md`

**Key file: `src/types/nodes.ts`**
```typescript
// Copy from Dev-Setup-Guide.md section "Phase 1.3"
// Make sure all types are complete and correct
```

**Done when**:
- All 12 node types defined (input, output, parse, filter, map, loop, if-else, try-catch, ai-gpt, ai-claude, variable, custom)
- Node colors and categories set
- Types export from index.ts
- Tests pass
- Documentation complete

**Time estimate**: 3 hours

---

### Wednesday, Dec 4
**Focus**: Zustand state management

**Tasks:**
- [ ] Create `src/components/Canvas/useNodeGraph.ts`
- [ ] Implement all state actions (addNode, removeNode, updateNode, etc.)
- [ ] Create `src/hooks/useUndoRedo.ts` with undo/redo stack
- [ ] Write unit tests for state management
- [ ] Test locally: create store, add/remove nodes

**Key actions to implement**:
- addNode(node)
- removeNode(nodeId)
- updateNode(nodeId, data)
- addEdge(edge)
- removeEdge(edgeId)
- selectNode(nodeId)
- undo()
- redo()
- clear()
- getGraph()
- loadGraph(graph)

**Done when**:
- useNodeGraph hook fully functional
- useUndoRedo hook works (10 undo levels)
- All tests pass
- Can add/remove/select nodes from console

**Time estimate**: 3 hours

---

### Thursday, Dec 5
**Focus**: Basic Canvas component

**Tasks:**
- [ ] Create `src/components/Canvas/Canvas.tsx`
- [ ] Set up ReactFlow with basic nodes
- [ ] Implement basic node rendering (no custom look yet)
- [ ] Connect to Zustand store
- [ ] Test: drag nodes, pan/zoom canvas

**Code structure**:
```typescript
// Canvas.tsx
- Import ReactFlow, useNodesState, useEdgesState
- Get nodes/edges from Zustand
- Set up onNodesChange, onEdgesChange callbacks
- Implement onConnect for edge creation
- Render ReactFlow component
```

**Done when**:
- Canvas renders with sample nodes
- Can drag nodes around
- Pan/zoom works
- Connections work (no validation yet)
- No TypeScript errors

**Time estimate**: 2 hours

---

### Friday, Dec 6
**Focus**: Custom Node component

**Tasks:**
- [ ] Create `src/components/Node/Node.tsx`
- [ ] Render node with ports (inputs/outputs)
- [ ] Add node type icon + color
- [ ] Implement accessible handles (for connections)
- [ ] Add tooltips for ports
- [ ] Style for neurodivergent accessibility

**Design principles**:
- Large hit targets (40px minimum)
- Color + icon (not text alone)
- Clear input/output indication
- High contrast
- Smooth animations

**Done when**:
- Nodes render with proper styling
- Ports are clickable
- Tooltips show on hover
- Keyboard accessible (Tab through ports)
- No accessibility warnings

**Time estimate**: 3 hours

---

### Saturday, Dec 7
**Focus**: Code generator & persistence

**Tasks:**
- [ ] Create `src/utils/codeGenerator.ts`
- [ ] Walk node graph → generate HyperCode text
- [ ] Implement save to JSON (`src/hooks/useLocalStorage.ts`)
- [ ] Implement load from JSON
- [ ] Write tests for code generation

**Code generation example**:
```
Visual:  [INPUT] → [PARSE] → [FILTER] → [OUTPUT]
Text:    data = INPUT(file) | PARSE(data) | FILTER(data, fn) | OUTPUT(data)
```

**Done when**:
- Can convert graph to HyperCode text
- Save/load works (localStorage)
- All conversions tested
- Sample programs generate correct code

**Time estimate**: 3 hours

---

### Sunday, Dec 8
**Focus**: Testing, docs, & push

**Tasks:**
- [ ] Write comprehensive unit tests
- [ ] Run coverage report (target: 80%+)
- [ ] Document all components in README
- [ ] Create CONTRIBUTING.md for other devs
- [ ] Final cleanup, formatting, TypeScript check
- [ ] Push everything to GitHub

**Tests to write**:
- useNodeGraph: add/remove/update nodes
- useUndoRedo: undo/redo functionality
- codeGenerator: visual → text conversion
- Canvas: rendering, interactions

**Done when**:
- All tests passing
- Coverage ≥ 80%
- No TypeScript errors
- README updated
- GitHub PR ready for review

**Time estimate**: 2-3 hours

---

## 📊 Week 1 Completion Checklist

**Code:**
- [ ] Project structure complete
- [ ] All TypeScript types defined
- [ ] Node schema with 12 types
- [ ] Zustand store fully functional
- [ ] Undo/redo working
- [ ] Canvas rendering nodes
- [ ] Custom node styling
- [ ] Code generator working
- [ ] Save/load functional
- [ ] All unit tests passing

**Documentation:**
- [ ] README.md updated
- [ ] CONTRIBUTING.md created
- [ ] Component documentation
- [ ] Type definitions documented
- [ ] Node schema documented

**Repository:**
- [ ] GitHub repo created
- [ ] All code committed
- [ ] PR template set up
- [ ] Issue templates ready

---

## 🎯 Success Criteria

By end of Week 1, you should be able to:

✅ Create a new visual program  
✅ Add nodes (all 12 types)  
✅ Connect nodes together  
✅ See the generated HyperCode text update in real-time  
✅ Save the program to localStorage  
✅ Load a saved program  
✅ Undo/redo actions  
✅ Press Tab to navigate all UI elements  
✅ Run all tests and get passing  

---

## 💻 Useful Commands

```bash
# Start dev server
npm run dev

# Run tests
npm run test

# Watch tests (run on file change)
npm run test:watch

# Coverage report
npm run test:coverage

# Type check
npx tsc --noEmit

# Format code
npm run format

# Lint
npm run lint

# Build
npm run build
```

---

## 🤝 If You Get Stuck

**Having issues?**

1. **First**: Check Dev-Setup-Guide.md for detailed code
2. **Then**: Look at reactflow docs: https://reactflow.dev
3. **Then**: Post in #hc-001-dev Discord
4. **Finally**: Create GitHub issue with error

**Don't get blocked for more than 30 minutes.**

---

## 📋 Resources in Your Inbox

- Dev-Setup-Guide.md (with full code examples)
- HyperCode-Windsurf.md (project vision)
- HC-001-task-breakdown.md (broader context)

---

## 🚀 Next Week Preview

Week 2-3 (Dec 9-22): You'll build:
- Node Palette (left sidebar)
- Properties Panel (right sidebar)
- Keyboard shortcuts
- Accessibility features
- Testing & refinement

---

## 💪 You Got This

This is a real project with real impact. **Every component you build enables neurodivergent coders.**

Questions? Ask. Stuck? Reach out. Done early? Grab a stretch task from the backlog.

**Let's ship. 🚀**

---

**Week 1 Status**: Ready to Start  
**Your Mission**: Build the Canvas  
**Deadline**: December 8, 2025  

**Now go code.** ✨