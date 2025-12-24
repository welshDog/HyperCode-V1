# task_manager.hc
# A reactive task manager with persistence

# State management
tasks = reactive(load_tasks() or [])
filter = reactive("all")  # all, active, completed

# Computed values
filtered_tasks = computed {
  tasks() | filter { task → 
    filter() == "all" || 
    (filter() == "active" && !task.completed) ||
    (filter() == "completed" && task.completed)
  }
}

remaining_count = computed {
  tasks() | filter { !_.completed } | length
}

# Actions
add_task = { text → 
  if text.trim() != "" {
    tasks.update(tasks => [
      ...tasks,
      {
        id: uuid(),
        text: text,
        completed: false,
        created_at: now()
      }
    ])
    save_tasks(tasks())
  }
}

toggle_task = { id → 
  tasks.update(tasks => 
    tasks | map { 
      if _.id == id { 
        { ..._, completed: !_.completed } 
      } else { 
        _ 
      }
    }
  )
  save_tasks(tasks())
}

clear_completed = {
  tasks.update(tasks => tasks | filter { !_.completed })
  save_tasks(tasks())
}

# UI Components
TaskItem = { task, on_toggle } → {
  <div class="task-item">
    <input 
      type="checkbox" 
      checked={task.completed} 
      on:change={() => on_toggle(task.id)}
    />
    <span class={task.completed ? "completed" : ""}>
      {task.text}
    </span>
  </div>
}

TaskList = { tasks, on_toggle } → {
  <div class="task-list">
    {tasks | map { task → 
      <TaskItem {task} {on_toggle} />
    }}
  </div>
}

# Main App
app = {
  <div class="task-app">
    <h1>HyperTask</h1>
    
    <div class="task-input">
      <input 
        type="text" 
        placeholder="What needs to be done?" 
        on:keydown={e → 
          if e.key == "Enter" {
            add_task(e.target.value)
            e.target.value = ""
          }
        }
      />
    </div>

    <div class="filters">
      <button 
        class={filter() == "all" ? "active" : ""}
        on:click={() => filter.set("all")}
      >
        All
      </button>
      <button 
        class={filter() == "active" ? "active" : ""}
        on:click={() => filter.set("active")}
      >
        Active
      </button>
      <button 
        class={filter() == "completed" ? "active" : ""}
        on:click={() => filter.set("completed")}
      >
        Completed
      </button>
    </div>

    <TaskList 
      tasks={filtered_tasks()} 
      on_toggle={toggle_task} 
    />

    <div class="footer">
      <span>{remaining_count()} items left</span>
      <button on:click={clear_completed}>
        Clear completed
      </button>
    </div>
  </div>
}

# Start the app
render(app, "#app")

# Persistence helpers
load_tasks = {
  try {
    localStorage.get("hyper-tasks") | json_parse()
  } catch {
    []
  }
}

save_tasks = { tasks → 
  tasks | json_stringify() | localStorage.set("hyper-tasks")
}