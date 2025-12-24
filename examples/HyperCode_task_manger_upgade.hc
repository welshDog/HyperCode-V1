# task_manager_enhanced.hc
# Enhanced Task Manager with Due Dates and Priorities

# Types
type Task = {
  id: string,
  text: string,
  completed: boolean,
  priority: "low" | "medium" | "high",
  due_date: Date | null,
  created_at: Date,
  category: string
}

# State
tasks = reactive(load_tasks() or [])
filter = reactive("all")  # all, active, completed, today, overdue
category_filter = reactive("all")
sort_by = reactive("due_date")  # due_date, priority, created_at

# Computed values
filtered_tasks = computed {
  tasks() 
    | filter { task → 
        (filter() == "all" || 
         (filter() == "active" && !task.completed) ||
         (filter() == "completed" && task.completed) ||
         (filter() == "today" && is_today(task.due_date)) ||
         (filter() == "overdue" && is_overdue(task.due_date))) &&
        (category_filter() == "all" || task.category == category_filter())
      }
    | sort { a, b → 
        switch sort_by() {
          "priority" → compare_priority(a.priority, b.priority),
          "created" → b.created_at - a.created_at,
          _ → (a.due_date || new Date(9999, 0, 1)) - 
               (b.due_date || new Date(9999, 0, 1))
        }
      }
}

# UI Components
PriorityBadge = { priority } → {
  const colors = {
    high: "red",
    medium: "orange",
    low: "green"
  }
  <span 
    class="priority-badge" 
    style={`background: ${colors[priority] || 'gray'}`}
  >
    {priority}
  </span>
}

DueDateBadge = { date } → {
  const today = new Date().toDateString()
  const task_date = date?.toDateString()
  const is_overdue = date && date < new Date() && task_date !== today
  
  <span 
    class={`due-date ${is_overdue ? 'overdue' : ''}`}
    title={date?.toLocaleString()}
  >
    {date ? format_date(date) : 'No due date'}
  </span>
}

# Add these new action handlers
add_task = { text, priority = "medium", due_date = null, category = "general" → 
  if text.trim() != "" {
    tasks.update(tasks => [
      ...tasks,
      {
        id: uuid(),
        text: text.trim(),
        completed: false,
        priority,
        due_date,
        category,
        created_at: new Date()
      }
    ])
    save_tasks()
  }
}

# New filter actions
set_filter = { filter_name → 
  filter.set(filter_name)
  # Auto-sort when changing to date-based filters
  if ["today", "overdue", "all"].includes(filter_name) {
    sort_by.set("due_date")
  }
}

# Save tasks helper with error handling
save_tasks = debounce(500, {
  try {
    const data = tasks() | map { task → 
      { 
        ...task, 
        due_date: task.due_date?.toISOString(),
        created_at: task.created_at.toISOString()
      }
    }
    localStorage.setItem("hyper-tasks", JSON.stringify(data))
  } catch (error) {
    console.error("Failed to save tasks:", error)
    # Show error to user
    show_notification("Failed to save tasks", "error")
  }
})

# Initialize with sample data if empty
effect {
  if (tasks().length == 0) {
    add_task("Try HyperCode", "high", add_days(new Date(), 1), "work")
    add_task("Learn reactive programming", "medium", add_days(new Date(), 3), "learning")
  }
}

# Enhanced UI with new features
app = {
  <div class="task-app">
    <header>
      <h1>✨ HyperTask Pro</h1>
      <div class="controls">
        <select on:change={e → sort_by.set(e.target.value)}>
          <option value="due_date">Sort by Due Date</option>
          <option value="priority">Sort by Priority</option>
          <option value="created">Sort by Created</option>
        </select>
        
        <select on:change={e → category_filter.set(e.target.value)}>
          <option value="all">All Categories</option>
          {get_unique_categories() | map { category → 
            <option value={category}>{category}</option>
          }}
        </select>
      </div>
    </header>

    <div class="filters">
      {["all", "active", "completed", "today", "overdue"] | map { filter_name → 
        <button 
          class={filter() == filter_name ? "active" : ""}
          on:click={() => set_filter(filter_name)}
        >
          {filter_name | capitalize}
        </button>
      }}
    </div>

    <TaskInput on_add={add_task} categories={get_unique_categories()} />
    
    <div class="stats">
      <span>{tasks() | filter { !_.completed } | length} tasks left</span>
      <span>{tasks() | filter { is_today(_.due_date) } | length} due today</span>
    </div>

    <TaskList 
      tasks={filtered_tasks()} 
      on_toggle={toggle_task}
      on_delete={delete_task}
    />
  </div>
}

# Start the app
render(app, "#app")