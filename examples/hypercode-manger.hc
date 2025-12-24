# task_manager_with_backend.hc
# Task Manager with Backend Integration

# Types
type Task = {
  id: string,
  text: string,
  completed: boolean,
  priority: "low" | "medium" | "high",
  due_date: string | null,
  created_at: string,
  category: string,
  version: number
}

# API Service
api = {
  base_url: "https://api.example.com/tasks",
  headers: {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${localStorage.get("auth_token")}`
  },

  # Fetch all tasks
  get_tasks: async { → 
    try {
      const response = await fetch(api.base_url, { headers: api.headers })
      if (!response.ok) throw new Error("Failed to fetch tasks")
      return await response.json()
    } catch (error) {
      console.error("API Error:", error)
      throw error
    }
  },

  # Create/Update task
  save_task: async { task → 
    const method = task.id ? "PUT" : "POST"
    const url = task.id ? `${api.base_url}/${task.id}` : api.base_url
    
    try {
      const response = await fetch(url, {
        method,
        headers: api.headers,
        body: JSON.stringify(task)
      })
      
      if (!response.ok) throw new Error("Failed to save task")
      return await response.json()
    } catch (error) {
      console.error("API Error:", error)
      throw error
    }
  },

  # Delete task
  delete_task: async { id → 
    try {
      const response = await fetch(`${api.base_url}/${id}`, {
        method: "DELETE",
        headers: api.headers
      })
      if (!response.ok) throw new Error("Failed to delete task")
      return true
    } catch (error) {
      console.error("API Error:", error)
      throw error
    }
  }
}

# State
tasks = reactive([])
loading = reactive(true)
error = reactive(null)
last_sync = reactive(null)

# Initialize and sync with backend
initialize = async {
  try {
    loading.set(true)
    const data = await api.get_tasks()
    tasks.set(data)
    last_sync.set(new Date())
  } catch (err) {
    error.set(err.message)
    # Fallback to local storage if offline
    const local_tasks = load_from_local_storage()
    if (local_tasks.length > 0) {
      tasks.set(local_tasks)
      show_notification("Using offline data", "warning")
    }
  } finally {
    loading.set(false)
  }
}

# Enhanced task operations with optimistic updates
add_task = async { task_data → 
  const temp_id = `temp_${Date.now()}`
  const new_task = {
    ...task_data,
    id: temp_id,
    created_at: new Date().toISOString(),
    version: 1
  }

  # Optimistic update
  tasks.update(tasks => [...tasks, new_task])
  
  try {
    const saved_task = await api.save_task(new_task)
    # Replace temp task with server response
    tasks.update(tasks => 
      tasks.map(t => t.id === temp_id ? saved_task : t)
    )
    save_to_local_storage()
    return saved_task
  } catch (err) {
    # Revert on error
    tasks.update(tasks => tasks.filter(t => t.id !== temp_id))
    throw err
  }
}

# Sync all local changes with the server
sync_with_backend = async {
  const local_tasks = load_from_local_storage("pending_changes") || []
  const results = []
  
  for (const task of local_tasks) {
    try {
      const result = await api.save_task(task)
      results.push({ success: true, data: result })
    } catch (err) {
      results.push({ success: false, error: err.message, task })
    }
  }
  
  if (results.every(r => r.success)) {
    localStorage.removeItem("pending_changes")
  }
  
  return results
}

# Offline support
setup_offline_support = {
  window.addEventListener("online", () => {
    if (navigator.onLine) {
      sync_with_backend().then(() => {
        show_notification("Changes synced with server", "success")
      })
    }
  })
}

# Initialize the app
initialize()
setup_offline_support()

# UI Component for sync status
SyncStatus = {
  <div class="sync-status">
    {loading() ? (
      <span class="syncing">🔄 Syncing...</span>
    ) : error() ? (
      <span class="error">⚠️ Offline - Changes saved locally</span>
    ) : (
      <span class="success">✅ Synced {format_time_ago(last_sync())}</span>
    )}
  </div>
}

# Main App with sync status
app = {
  <div class="task-app">
    <header>
      <h1>📡 Task Manager Pro</h1>
      <SyncStatus />
    </header>
    
    {/* Rest of your UI components */}
    <TaskList 
      tasks={filtered_tasks()} 
      on_toggle={toggle_task}
      on_delete={delete_task}
      loading={loading()}
    />
    
    <button 
      on:click={sync_with_backend}
      disabled={loading()}
    >
      {loading() ? "Syncing..." : "Sync Now"}
    </button>
  </div>
}

# Start the app
render(app, "#app")