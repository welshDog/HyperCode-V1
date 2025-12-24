# database_integration.hc
# HyperCode Database Integration Example

# === Database Configuration ===
db = database.connect({
  provider: "hyperdb",  # Could be sqlite, postgres, etc.
  path: "./data/hypercode.db",
  schema: {
    # Define your database schema
    tasks: {
      id: "primary_key",
      title: "string",
      description: "text",
      status: "string",
      priority: "integer",
      created_at: "datetime",
      updated_at: "datetime"
    },
    # Add more tables as needed
  }
})

# === Example: Task Management with Database ===

# Create a new task
create_task = { title, description, priority=1 →
  db.transaction {
    const task = db.tasks.insert({
      title,
      description,
      status: "pending",
      priority,
      created_at: new Date(),
      updated_at: new Date()
    })
    return task
  }
}

# Update task status
update_task_status = { id, status →
  db.transaction {
    db.tasks
      .where("id").equals(id)
      .update({
        status,
        updated_at: new Date()
      })
  }
}

# Query tasks with filters
get_tasks = { filters={} →
  let query = db.tasks
  
  # Apply filters
  if (filters.status) {
    query = query.where("status").equals(filters.status)
  }
  
  if (filters.priority) {
    query = query.where("priority").equals(filters.priority)
  }
  
  if (filters.search) {
    const search = filters.search.toLowerCase()
    query = query.filter(task => 
      task.title.toLowerCase().includes(search) ||
      task.description.toLowerCase().includes(search)
    )
  }
  
  # Execute query
  return query.toArray()
}

# === Real-time Data Sync ===

# Subscribe to task changes
task_updates = db.tasks
  .changes()
  .on("create", task => console.log("New task:", task))
  .on("update", task => console.log("Updated task:", task))
  .on("delete", id => console.log("Deleted task:", id))

# === Example Usage ===

# Create some tasks
create_task("Implement auth", "Add user authentication")
create_task("Fix login bug", "Users can't login on mobile", 2)

# Get all high priority tasks
high_priority = get_tasks({ priority: 1 })

# Search for tasks
search_results = get_tasks({ search: "auth" })

# Update a task
update_task_status(1, "in_progress")

# === Data Export/Import ===

# Export to JSON
export_data = {
  const data = {
    tasks: await db.tasks.toArray(),
    exported_at: new Date().toISOString()
  }
  return JSON.stringify(data, null, 2)
}

# Import from JSON
import_data = { json_string →
  const data = JSON.parse(json_string)
  return db.transaction(() => {
    return db.tasks.bulkAdd(data.tasks)
  })
}

# === Database Maintenance ===

# Backup database
backup_database = {
  const backup_file = `backup_${Date.now()}.db`
  return db.export(backup_file)
}

# Compact database (if supported)
optimize_database = {
  return db.maintenance.compact()
}

# === Error Handling ===
try {
  // Database operations
} catch (error) {
  if (error.name === "ConstraintError") {
    console.error("Database constraint violated:", error.message)
  } else {
    console.error("Database error:", error)
  }
}