// HyperCode - Neurodivergent-Friendly Visual Coding Platform

// ==================== DATA MODELS ====================

const nodeTypes = {
  function: {
    color: "#4A90E2",
    icon: "ƒ",
    description: "Function block",
    codeTemplate: "def my_function():\n    pass",
  },
  loop: {
    color: "#50C878",
    icon: "⟲",
    description: "Loop block",
    codeTemplate: "for i in range(10):\n    pass",
  },
  condition: {
    color: "#F39C12",
    icon: "?",
    description: "Conditional block",
    codeTemplate: "if condition:\n    pass",
  },
  data: {
    color: "#9B59B6",
    icon: "□",
    description: "Data block",
    codeTemplate: "data = None",
  },
  output: {
    color: "#E74C3C",
    icon: "→",
    description: "Output block",
    codeTemplate: "print(result)",
  },
};

const sampleTasks = [
  { title: "Create main function", status: "done", time: 15 },
  { title: "Add input validation", status: "in-progress", time: 20 },
  { title: "Connect to output", status: "todo", time: 10 },
];

const accessibilityPresets = {
  adhd: { theme: "dark", animations: 0, fontSize: "large" },
  autism: { theme: "high-contrast", animations: 0, fontSize: "medium" },
  dyslexia: { theme: "light", font: "opendyslexic", fontSize: "large" },
};

// ==================== STATE MANAGEMENT ====================

const state = {
  nodes: [],
  connections: [],
  tasks: [...sampleTasks],
  selectedNode: null,
  nextNodeId: 1,
  focusMode: false,
  theme: "dark",
  animationSpeed: 100,
  fontSize: "medium",
  useOpenDyslexic: false,
  draggedNode: null,
  dragOffset: { x: 0, y: 0 },
  connectingFrom: null,
};

// ==================== INITIALIZATION ====================

function init() {
  setupEventListeners();
  renderTasks();
  updateProgress();

  // Add sample nodes
  addNode("function", 100, 100);
  addNode("data", 300, 150);

  updateCode();
  announce("HyperCode initialized. Visual coding environment ready.");
}

// ==================== EVENT LISTENERS ====================

function setupEventListeners() {
  // Theme buttons
  document
    .getElementById("theme-light")
    .addEventListener("click", () => setTheme("light"));
  document
    .getElementById("theme-dark")
    .addEventListener("click", () => setTheme("dark"));
  document
    .getElementById("theme-contrast")
    .addEventListener("click", () => setTheme("high-contrast"));

  // Focus mode
  document.getElementById("focus-mode").addEventListener("click", toggleFocusMode);

  // Sidebar toggles
  document.getElementById("toggle-sidebar-left").addEventListener("click", () => {
    document.querySelector(".sidebar").classList.toggle("collapsed");
  });
  document.getElementById("toggle-sidebar-right").addEventListener("click", () => {
    document.querySelector(".sidebar-right").classList.toggle("collapsed");
  });

  // Panel toggle
  document.getElementById("toggle-panel").addEventListener("click", () => {
    const panel = document.getElementById("bottom-panel");
    panel.classList.toggle("collapsed");
    document.getElementById("toggle-panel").textContent = panel.classList.contains(
      "collapsed",
    )
      ? "▲"
      : "▼";
  });

  // Node type buttons
  document.querySelectorAll("[data-node-type]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const type = e.currentTarget.getAttribute("data-node-type");
      const x = Math.random() * 400 + 100;
      const y = Math.random() * 300 + 100;
      addNode(type, x, y);
      announce(`${nodeTypes[type].description} added to canvas`);
    });
  });

  // Run code
  document.getElementById("run-code").addEventListener("click", runCode);

  // Clear canvas
  document.getElementById("clear-canvas").addEventListener("click", () => {
    if (confirm("Clear all nodes?")) {
      state.nodes = [];
      state.connections = [];
      renderNodes();
      updateCode();
      announce("Canvas cleared");
    }
  });

  // Add task form
  document.getElementById("add-task-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const title = document.getElementById("new-task-title").value.trim();
    const time = parseInt(document.getElementById("new-task-time").value) || 10;

    if (title) {
      state.tasks.push({ title, status: "todo", time });
      renderTasks();
      updateProgress();
      document.getElementById("new-task-title").value = "";
      document.getElementById("new-task-time").value = "";
      announce(`Task "${title}" added`);
    }
  });

  // Font size
  document.getElementById("font-size-select").addEventListener("change", (e) => {
    setFontSize(e.target.value);
  });

  // OpenDyslexic font
  document.getElementById("opendyslexic-font").addEventListener("change", (e) => {
    state.useOpenDyslexic = e.target.checked;
    document.body.classList.toggle("font-opendyslexic", e.target.checked);
    announce(e.target.checked ? "OpenDyslexic font enabled" : "Default font restored");
  });

  // Animation speed
  document.getElementById("animation-speed").addEventListener("input", (e) => {
    const value = e.target.value;
    document.getElementById("animation-value").textContent = value;
    state.animationSpeed = value;
    document.documentElement.style.setProperty("--animation-speed", value / 100);

    if (value === "0") {
      document.body.classList.add("no-animations");
    } else {
      document.body.classList.remove("no-animations");
    }
  });

  // Preset buttons
  document.querySelectorAll("[data-preset]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const preset = e.currentTarget.getAttribute("data-preset");
      applyPreset(preset);
    });
  });

  // Esoteric info toggle
  document.getElementById("toggle-esoteric").addEventListener("click", (e) => {
    const info = document.getElementById("esoteric-info");
    const isVisible = info.style.display !== "none";
    info.style.display = isVisible ? "none" : "block";
    e.target.textContent = isVisible ? "Show Influences" : "Hide Influences";
  });

  // Voice command
  document.getElementById("voice-fab").addEventListener("click", () => {
    const panel = document.getElementById("voice-panel");
    panel.classList.toggle("active");
    if (panel.classList.contains("active")) {
      document.getElementById("voice-input").focus();
    }
  });

  document
    .getElementById("voice-submit")
    .addEventListener("click", processVoiceCommand);
  document.getElementById("voice-input").addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      processVoiceCommand();
    }
  });

  // Keyboard shortcuts
  document.addEventListener("keydown", (e) => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;

    if (e.key === "f" || e.key === "F") {
      toggleFocusMode();
    } else if (e.key === "r" || e.key === "R") {
      runCode();
    } else if (e.key === "Delete" && state.selectedNode) {
      deleteNode(state.selectedNode);
    }
  });

  // Canvas interactions
  const canvas = document.getElementById("canvas-content");
  canvas.addEventListener("mousedown", handleCanvasMouseDown);
  canvas.addEventListener("mousemove", handleCanvasMouseMove);
  canvas.addEventListener("mouseup", handleCanvasMouseUp);
}

// ==================== NODE MANAGEMENT ====================

function addNode(type, x, y) {
  const node = {
    id: state.nextNodeId++,
    type,
    x,
    y,
    data: {
      name: `${type}_${state.nextNodeId}`,
    },
  };

  state.nodes.push(node);
  renderNodes();
  updateCode();
}

function renderNodes() {
  const container = document.getElementById("canvas-content");
  container.querySelectorAll(".node").forEach((el) => el.remove());

  state.nodes.forEach((node) => {
    const nodeEl = createNodeElement(node);
    container.appendChild(nodeEl);
  });

  renderConnections();
}

function createNodeElement(node) {
  const div = document.createElement("div");
  div.className = "node";
  div.id = `node-${node.id}`;
  div.style.left = `${node.x}px`;
  div.style.top = `${node.y}px`;
  div.style.borderColor = nodeTypes[node.type].color;
  div.setAttribute("data-node-id", node.id);
  div.setAttribute("role", "button");
  div.setAttribute("tabindex", "0");
  div.setAttribute("aria-label", `${nodeTypes[node.type].description} node`);

  const typeInfo = nodeTypes[node.type];

  div.innerHTML = `
    <div class="node-header">
      <span class="node-icon" style="color: ${typeInfo.color}">${typeInfo.icon}</span>
      <span class="node-title">${node.data.name}</span>
    </div>
    <div class="node-content">${typeInfo.description}</div>
    <div class="node-code">${typeInfo.codeTemplate.split("\n")[0]}</div>
    <div class="node-ports">
      <div class="node-port input-port" data-port="input"></div>
      <div class="node-port output-port" data-port="output"></div>
    </div>
  `;

  // Node selection
  div.addEventListener("click", (e) => {
    if (e.target.classList.contains("node-port")) return;
    selectNode(node.id);
  });

  // Port connections
  div.querySelectorAll(".node-port").forEach((port) => {
    port.addEventListener("click", (e) => {
      e.stopPropagation();
      handlePortClick(node.id, e.target.getAttribute("data-port"));
    });
  });

  return div;
}

function selectNode(nodeId) {
  state.selectedNode = nodeId;
  document.querySelectorAll(".node").forEach((el) => {
    el.classList.remove("selected");
  });
  document.getElementById(`node-${nodeId}`)?.classList.add("selected");
}

function deleteNode(nodeId) {
  state.nodes = state.nodes.filter((n) => n.id !== nodeId);
  state.connections = state.connections.filter(
    (c) => c.from !== nodeId && c.to !== nodeId,
  );
  state.selectedNode = null;
  renderNodes();
  updateCode();
  announce("Node deleted");
}

function handlePortClick(nodeId, portType) {
  if (portType === "output") {
    state.connectingFrom = nodeId;
    announce("Select an input port to connect to");
  } else if (portType === "input" && state.connectingFrom) {
    addConnection(state.connectingFrom, nodeId);
    state.connectingFrom = null;
    announce("Nodes connected");
  }
}

function addConnection(fromId, toId) {
  if (!state.connections.find((c) => c.from === fromId && c.to === toId)) {
    state.connections.push({ from: fromId, to: toId });
    renderConnections();
    updateCode();
  }
}

function renderConnections() {
  const svg = document.getElementById("connections-svg");
  svg.innerHTML = "";

  state.connections.forEach((conn) => {
    const fromNode = document.getElementById(`node-${conn.from}`);
    const toNode = document.getElementById(`node-${conn.to}`);

    if (!fromNode || !toNode) return;

    const fromRect = fromNode.getBoundingClientRect();
    const toRect = toNode.getBoundingClientRect();
    const canvasRect = document
      .getElementById("canvas-content")
      .getBoundingClientRect();

    const x1 = fromRect.left - canvasRect.left + fromRect.width;
    const y1 = fromRect.top - canvasRect.top + fromRect.height / 2;
    const x2 = toRect.left - canvasRect.left;
    const y2 = toRect.top - canvasRect.top + toRect.height / 2;

    const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    const midX = (x1 + x2) / 2;
    const d = `M ${x1} ${y1} C ${midX} ${y1}, ${midX} ${y2}, ${x2} ${y2}`;
    path.setAttribute("d", d);
    path.setAttribute("class", "connection-line");
    svg.appendChild(path);
  });
}

// ==================== DRAG AND DROP ====================

function handleCanvasMouseDown(e) {
  const nodeEl = e.target.closest(".node");
  if (!nodeEl) return;

  const nodeId = parseInt(nodeEl.getAttribute("data-node-id"));
  const node = state.nodes.find((n) => n.id === nodeId);
  if (!node) return;

  state.draggedNode = node;
  const rect = nodeEl.getBoundingClientRect();
  state.dragOffset = {
    x: e.clientX - rect.left,
    y: e.clientY - rect.top,
  };

  nodeEl.classList.add("dragging");
  e.preventDefault();
}

function handleCanvasMouseMove(e) {
  if (!state.draggedNode) return;

  const canvas = document.getElementById("canvas-content");
  const rect = canvas.getBoundingClientRect();

  state.draggedNode.x = e.clientX - rect.left - state.dragOffset.x;
  state.draggedNode.y = e.clientY - rect.top - state.dragOffset.y;

  const nodeEl = document.getElementById(`node-${state.draggedNode.id}`);
  nodeEl.style.left = `${state.draggedNode.x}px`;
  nodeEl.style.top = `${state.draggedNode.y}px`;

  renderConnections();
}

function handleCanvasMouseUp(e) {
  if (state.draggedNode) {
    const nodeEl = document.getElementById(`node-${state.draggedNode.id}`);
    nodeEl?.classList.remove("dragging");
    state.draggedNode = null;
  }
}

// ==================== CODE GENERATION ====================

function updateCode() {
  let code = "# Generated Python Code\n\n";

  if (state.nodes.length === 0) {
    code = "# No nodes yet. Add nodes to generate code!";
  } else {
    // Sort nodes by connections to create logical flow
    const sorted = topologicalSort();

    sorted.forEach((nodeId, index) => {
      const node = state.nodes.find((n) => n.id === nodeId);
      if (node) {
        const typeInfo = nodeTypes[node.type];
        code += `# ${node.data.name}\n`;
        code += typeInfo.codeTemplate + "\n\n";
      }
    });

    if (state.connections.length > 0) {
      code += "# Connections:\n";
      state.connections.forEach((conn) => {
        const from = state.nodes.find((n) => n.id === conn.from);
        const to = state.nodes.find((n) => n.id === conn.to);
        if (from && to) {
          code += `# ${from.data.name} -> ${to.data.name}\n`;
        }
      });
    }
  }

  document.getElementById("code-display").textContent = code;
}

function topologicalSort() {
  // Simple topological sort for node ordering
  const visited = new Set();
  const result = [];

  function visit(nodeId) {
    if (visited.has(nodeId)) return;
    visited.add(nodeId);

    // Visit children first
    state.connections.filter((c) => c.from === nodeId).forEach((c) => visit(c.to));

    result.unshift(nodeId);
  }

  state.nodes.forEach((node) => visit(node.id));
  return result;
}

function runCode() {
  const consoleEl = document.getElementById("console-output");
  consoleEl.innerHTML = "";

  addConsoleLine("▶️ Running code...", "info");

  setTimeout(() => {
    if (state.nodes.length === 0) {
      addConsoleLine("⚠️ No nodes to execute", "error");
      return;
    }

    addConsoleLine("✅ Parsing nodes...", "success");

    state.nodes.forEach((node) => {
      addConsoleLine(`  • Executing ${node.data.name} (${node.type})`, "info");
    });

    if (state.connections.length > 0) {
      addConsoleLine("✅ Processing connections...", "success");
      state.connections.forEach((conn) => {
        const from = state.nodes.find((n) => n.id === conn.from);
        const to = state.nodes.find((n) => n.id === conn.to);
        if (from && to) {
          addConsoleLine(`  • ${from.data.name} → ${to.data.name}`, "info");
        }
      });
    }

    addConsoleLine("✅ Execution complete!", "success");
    addConsoleLine(`Result: Generated ${state.nodes.length} operations`, "success");

    announce("Code execution complete");
  }, 500);
}

function addConsoleLine(text, type = "info") {
  const consoleEl = document.getElementById("console-output");
  const line = document.createElement("div");
  line.className = `console-line ${type}`;
  line.textContent = text;
  consoleEl.appendChild(line);
  consoleEl.scrollTop = consoleEl.scrollHeight;
}

// ==================== TASK MANAGEMENT ====================

function renderTasks() {
  const container = document.getElementById("task-list");
  container.innerHTML = "";

  state.tasks.forEach((task, index) => {
    const taskEl = document.createElement("div");
    taskEl.className = "task-item";

    taskEl.innerHTML = `
      <div class="task-header">
        <span class="task-title">${task.title}</span>
        <span class="task-status status-${task.status}">${task.status}</span>
      </div>
      <div class="task-time">⏱️ ${task.time} minutes</div>
      <div class="task-actions">
        ${
          task.status !== "done"
            ? `<button class="btn btn-sm btn-primary" data-task-index="${index}" data-action="done">✓ Complete</button>`
            : ""
        }
        ${
          task.status === "todo"
            ? `<button class="btn btn-sm" data-task-index="${index}" data-action="progress">▶️ Start</button>`
            : ""
        }
        <button class="btn btn-sm" data-task-index="${index}" data-action="delete">🗑️</button>
      </div>
    `;

    container.appendChild(taskEl);
  });

  // Task action buttons
  container.querySelectorAll("[data-action]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const index = parseInt(e.currentTarget.getAttribute("data-task-index"));
      const action = e.currentTarget.getAttribute("data-action");
      handleTaskAction(index, action);
    });
  });
}

function handleTaskAction(index, action) {
  const task = state.tasks[index];

  if (action === "done") {
    task.status = "done";
    renderTasks();
    updateProgress();
    celebrate();
    announce(`Task "${task.title}" completed!`);
  } else if (action === "progress") {
    task.status = "in-progress";
    renderTasks();
    updateProgress();
    announce(`Task "${task.title}" started`);
  } else if (action === "delete") {
    state.tasks.splice(index, 1);
    renderTasks();
    updateProgress();
    announce("Task deleted");
  }
}

function updateProgress() {
  const done = state.tasks.filter((t) => t.status === "done").length;
  const total = state.tasks.length;
  const percent = total > 0 ? (done / total) * 100 : 0;

  document.getElementById("overall-progress").style.width = `${percent}%`;
}

function celebrate() {
  if (state.animationSpeed > 0) {
    const taskList = document.getElementById("task-list");
    taskList.classList.add("celebrating");
    setTimeout(() => taskList.classList.remove("celebrating"), 500);
  }
}

// ==================== VOICE COMMANDS ====================

function processVoiceCommand() {
  const input = document.getElementById("voice-input").value.toLowerCase().trim();
  const feedback = document.getElementById("voice-feedback");

  if (!input) return;

  let executed = false;
  let message = "";

  if (input.includes("create function") || input.includes("add function")) {
    addNode("function", Math.random() * 400 + 100, Math.random() * 300 + 100);
    message = "Function node created";
    executed = true;
  } else if (input.includes("add loop") || input.includes("create loop")) {
    addNode("loop", Math.random() * 400 + 100, Math.random() * 300 + 100);
    message = "Loop node created";
    executed = true;
  } else if (input.includes("add condition") || input.includes("create condition")) {
    addNode("condition", Math.random() * 400 + 100, Math.random() * 300 + 100);
    message = "Condition node created";
    executed = true;
  } else if (input.includes("add data") || input.includes("create data")) {
    addNode("data", Math.random() * 400 + 100, Math.random() * 300 + 100);
    message = "Data node created";
    executed = true;
  } else if (input.includes("add output") || input.includes("create output")) {
    addNode("output", Math.random() * 400 + 100, Math.random() * 300 + 100);
    message = "Output node created";
    executed = true;
  } else if (input.includes("focus mode") || input.includes("enable focus")) {
    toggleFocusMode();
    message = state.focusMode ? "Focus mode enabled" : "Focus mode disabled";
    executed = true;
  } else if (input.includes("run code") || input.includes("execute")) {
    runCode();
    message = "Running code";
    executed = true;
  } else if (input.includes("clear canvas") || input.includes("clear all")) {
    state.nodes = [];
    state.connections = [];
    renderNodes();
    updateCode();
    message = "Canvas cleared";
    executed = true;
  } else if (input.includes("connect nodes")) {
    if (state.nodes.length >= 2) {
      addConnection(state.nodes[0].id, state.nodes[1].id);
      message = "Nodes connected";
      executed = true;
    } else {
      message = "Need at least 2 nodes to connect";
      executed = true;
    }
  }

  if (executed) {
    feedback.textContent = `✓ ${message}`;
    feedback.classList.add("active");
    announce(message);

    setTimeout(() => {
      feedback.classList.remove("active");
    }, 3000);

    document.getElementById("voice-input").value = "";
  } else {
    feedback.textContent = "❌ Command not recognized";
    feedback.style.borderColor = "var(--color-error)";
    feedback.style.color = "var(--color-error)";
    feedback.classList.add("active");

    setTimeout(() => {
      feedback.classList.remove("active");
      feedback.style.borderColor = "";
      feedback.style.color = "";
    }, 3000);
  }
}

// ==================== THEME & ACCESSIBILITY ====================

function setTheme(theme) {
  state.theme = theme;
  document.documentElement.setAttribute("data-theme", theme);

  // Update active button
  document.querySelectorAll('[id^="theme-"]').forEach((btn) => {
    btn.classList.remove("active");
  });
  document.getElementById(`theme-${theme}`).classList.add("active");

  announce(`${theme} theme activated`);
}

function setFontSize(size) {
  state.fontSize = size;
  document.body.className = document.body.className.replace(/font-\w+/g, "");
  document.body.classList.add(`font-${size}`);
  if (state.useOpenDyslexic) {
    document.body.classList.add("font-opendyslexic");
  }
  announce(`Font size set to ${size}`);
}

function toggleFocusMode() {
  state.focusMode = !state.focusMode;
  document.body.classList.toggle("focus-mode", state.focusMode);
  document.getElementById("focus-mode").classList.toggle("active", state.focusMode);
  document.getElementById("focus-mode").setAttribute("aria-pressed", state.focusMode);
  announce(state.focusMode ? "Focus mode enabled" : "Focus mode disabled");
}

function applyPreset(presetName) {
  const preset = accessibilityPresets[presetName];
  if (!preset) return;

  // Apply theme
  if (preset.theme) {
    setTheme(preset.theme);
  }

  // Apply animations
  if (preset.animations !== undefined) {
    state.animationSpeed = preset.animations;
    document.getElementById("animation-speed").value = preset.animations;
    document.getElementById("animation-value").textContent = preset.animations;
    document.documentElement.style.setProperty(
      "--animation-speed",
      preset.animations / 100,
    );
    document.body.classList.toggle("no-animations", preset.animations === 0);
  }

  // Apply font size
  if (preset.fontSize) {
    setFontSize(preset.fontSize);
    document.getElementById("font-size-select").value = preset.fontSize;
  }

  // Apply font type
  if (preset.font === "opendyslexic") {
    state.useOpenDyslexic = true;
    document.body.classList.add("font-opendyslexic");
    document.getElementById("opendyslexic-font").checked = true;
  }

  announce(`${presetName.toUpperCase()}-friendly preset applied`);
}

// ==================== ACCESSIBILITY ====================

function announce(message) {
  const announcer = document.getElementById("sr-announcements");
  announcer.textContent = message;

  // Clear after announcement
  setTimeout(() => {
    announcer.textContent = "";
  }, 1000);
}

// ==================== START APPLICATION ====================

document.addEventListener("DOMContentLoaded", init);
