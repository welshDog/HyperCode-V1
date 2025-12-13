# 🚀 Developer Quickstart - START HERE

## Your Mission
Build the **React visual programming canvas** for HyperCode's HC-001.

**You have 3 minutes. Read this.**

---

## What You're Building

A node-based visual editor where neurodivergent coders can:
1. Drag nodes onto canvas
2. Connect nodes together
3. See HyperCode text generate in real-time
4. Save/load programs

**Example workflow:**
```
[INPUT file] → [PARSE JSON] → [FILTER items] → [OUTPUT results]
```

---

## Your Weekly Tasks (Dec 2-8)

| Day | Task | Time |
|-----|------|------|
| **Mon 12/2** | Project setup, Git init | 2h |
| **Tue 12/3** | TypeScript types + node schema | 3h |
| **Wed 12/4** | Zustand state management | 3h |
| **Thu 12/5** | Basic Canvas component | 2h |
| **Fri 12/6** | Custom Node styling | 3h |
| **Sat 12/7** | Code generator + save/load | 3h |
| **Sun 12/8** | Tests, docs, push to GitHub | 2-3h |

**Total: ~19 hours this week**

---

## Right Now (Next 30 Minutes)

### Step 1: Create Project
```bash
npm create vite@latest hypercode-visual -- --template react-ts
cd hypercode-visual
npm install
```

### Step 2: Install Dependencies
```bash
npm install reactflow zustand react-icons axios
npm install -D tailwindcss postcss autoprefixer vitest @testing-library/react
npx tailwindcss init -p
```

### Step 3: Create Folder Structure
```
src/
├── components/
│   ├── Canvas/
│   ├── Node/
│   ├── Palette/
│   └── PropertiesPanel/
├── hooks/
├── utils/
├── types/
└── styles/
```

### Step 4: Start Dev Server
```bash
npm run dev
```

**You're ready when**: App opens in browser at `localhost:5173`

---

## Your Tech Stack

- **reactflow** - Node/edge library (battle-tested)
- **zustand** - State management (lightweight)
- **TypeScript** - Type safety
- **Tailwind** - Styling
- **Vitest** - Testing

---

## Key Files You'll Create

**This Week (Week 1):**

1. `src/types/nodes.ts` - TypeScript types
2. `src/utils/nodeSchema.ts` - 12 node definitions
3. `src/components/Canvas/useNodeGraph.ts` - Zustand store
4. `src/components/Canvas/Canvas.tsx` - Main canvas
5. `src/components/Node/Node.tsx` - Custom node component
6. `src/utils/codeGenerator.ts` - Visual → HyperCode text
7. `tests/` - Unit tests

---

## Success = This Works

By Dec 8, you should be able to:

```
1. Drag node from palette to canvas ✅
2. Connect two nodes ✅
3. See live code output update ✅
4. Press Ctrl+Z to undo ✅
5. Save program to localStorage ✅
6. All tests passing ✅
```

---

## Your Daily Playbook

**Every day:**

1. **Morning** (5 min): Read the daily task in Week-1-Daily-Checklist.md
2. **Work** (2-3h): Build the day's task
3. **Test** (30 min): Run tests, check TypeScript
4. **Commit** (10 min): `git add . && git commit -m "Day X: [task]"`
5. **Review** (10 min): Code looks clean? Add comments? Ready for feedback?

---

## If You Get Stuck (< 30 min)

**Problem: React won't start**
- Check Node version: `node --version` (need 18+)
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`

**Problem: TypeScript errors**
- Check `tsconfig.json` exists
- Run `npx tsc --noEmit` to see all errors

**Problem: Don't know how to implement something**
- Check Dev-Setup-Guide.md (has code examples)
- Check reactflow docs: https://reactflow.dev
- Post in Discord #hc-001-dev

**> 30 min stuck? Reach out immediately. That's what the team is for.**

---

## Resources Right Here

You have:
- ✅ Dev-Setup-Guide.md (detailed code)
- ✅ Week-1-Daily-Checklist.md (day-by-day tasks)
- ✅ HyperCode-Windsurf.md (why this matters)
- ✅ HC-001-task-breakdown.md (full context)

---

## Keyboard Shortcut: Ask Windsurf

When you have questions, paste into Windsurf:

```
"I'm building HC-001 Visual Editor with React + reactflow.
[Problem description]

Based on the Dev-Setup-Guide.md, how would you solve this?"
```

Windsurf will instantly understand the architecture and suggest code.

---

## Go Time

**Right now:**

1. Run: `npm create vite@latest hypercode-visual -- --template react-ts`
2. Run: `npm install` (the dependency list)
3. Run: `npm run dev`
4. Open `localhost:5173` in browser
5. See React logo? ✅ You're ready
6. Jump to Week-1-Daily-Checklist.md Monday tasks
7. Start building

**You have this. 30 minutes to get set up. Then we build.** 💪

---

## Questions?

- Discord: #hc-001-dev
- GitHub: Post issues in HC-001 project
- Slack/Email: Direct message (we'll get back fast)

---

## Remember

You're not just building UI. You're building the gateway that lets neurodivergent coders express spatial logic visually. Every node you render is someone's breakthrough moment.

Ship it. Ship it right. Make it accessible.

**Let's go.** 🚀

---

**Created**: Dec 2, 2025 6:06 PM GMT  
**Status**: Ready  
**Next**: npm create vite...  
**Go.** ✨