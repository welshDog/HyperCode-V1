# 📝 Todo List Web App in HyperCode
# A complete web application demonstrating HyperCode's neurodivergent-friendly syntax

import { WebApp, Database, UI } from hypercode:web
import { DateTime, Validation } from hypercode:utils

# 🎨 Todo App Configuration
todo_app WebApp {
    name: "Neurodivergent Todo App"
    description: "A clean, visual todo list app designed for focus and clarity"
    
    # 🧠 Accessibility-first UI design
    ui: {
        theme: "high_contrast"
        font_size: "large"
        animations: "minimal"
        colors: {
            primary: "#2563eb"      # Calm blue
            success: "#16a34a"      # Clear green  
            warning: "#f59e0b"      # Warm orange
            danger: "#dc2626"       # Clear red
            background: "#ffffff"   # Clean white
            text: "#1f2937"         # Dark gray
        }
    }
    
    # 🗄️ Database setup
    database: todo_db
    
    # 🌐 Routes with visual clarity
    routes: [
        GET / => show_home()
        GET /todos => show_all_todos()
        POST /todos => create_todo()
        PUT /todos/[id] => update_todo(id)
        DELETE /todos/[id] => delete_todo(id)
        GET /todos/completed => show_completed()
        GET /todos/pending => show_pending()
    ]
}

# 📊 Database Schema (visual structure)
todo_db Database {
    type: "sqlite"
    path: "./todo_app.db"
    
    tables: {
        todos: {
            id: INTEGER PRIMARY_KEY
            title: TEXT NOT_NULL
            description: TEXT
            status: TEXT DEFAULT "pending"  # pending, completed, cancelled
            priority: TEXT DEFAULT "medium" # low, medium, high
            created_at: TIMESTAMP DEFAULT_NOW
            completed_at: TIMESTAMP NULL
            due_date: DATE NULL
            tags: TEXT  # JSON array of tags
        }
    }
}

# 🎯 Todo Management Functions

function show_home() {
    # 🏠 Home page with clear overview
    stats ← get_todo_statistics()
    
    return UI.page({
        title: "📝 Todo Dashboard"
        content: [
            UI.header("📝 Your Todo Dashboard", level: 1)
            
            # 📊 Statistics cards (visual layout)
            UI.grid([
                UI.card({
                    icon: "📋"
                    title: "Total Tasks"
                    value: stats.total
                    color: "primary"
                })
                UI.card({
                    icon: "✅"
                    title: "Completed"
                    value: stats.completed
                    color: "success"
                })
                UI.card({
                    icon: "⏳"
                    title: "Pending"
                    value: stats.pending
                    color: "warning"
                })
                UI.card({
                    icon: "🔥"
                    title: "High Priority"
                    value: stats.high_priority
                    color: "danger"
                })
            ])
            
            # ➕ Quick add form
            UI.section({
                title: "➕ Quick Add Task"
                content: UI.form({
                    action: "/todos"
                    method: "POST"
                    fields: [
                        UI.input({
                            name: "title"
                            label: "📝 Task Title"
                            placeholder: "What needs to be done?"
                            required: true
                            autofocus: true
                        })
                        UI.textarea({
                            name: "description"
                            label: "📄 Description"
                            placeholder: "Add more details (optional)"
                        })
                        UI.select({
                            name: "priority"
                            label: "🎯 Priority"
                            options: [
                                {value: "low", label: "🟢 Low"}
                                {value: "medium", label: "🟡 Medium"}
                                {value: "high", label: "🔴 High"}
                            ]
                            default: "medium"
                        })
                        UI.input({
                            name: "due_date"
                            label: "📅 Due Date"
                            type: "date"
                        })
                    ]
                    button: UI.button({
                        text: "➕ Add Task"
                        style: "primary"
                        icon: "plus"
                    })
                })
            })
            
            # 📋 Recent tasks
            UI.section({
                title: "📋 Recent Tasks"
                content: render_todo_list(get_recent_todos(5))
            })
        ]
    })
}

function show_all_todos() {
    # 📋 Show all todos with filtering options
    todos ← get_all_todos()
    
    return UI.page({
        title: "📋 All Tasks"
        content: [
            UI.header("📋 All Your Tasks", level: 1)
            
            # 🔍 Filter controls
            UI.filter_bar({
                filters: [
                    {name: "status", label: "Status", options: ["all", "pending", "completed"]}
                    {name: "priority", label: "Priority", options: ["all", "low", "medium", "high"]}
                    {name: "sort", label: "Sort", options: ["created_desc", "created_asc", "due_date", "priority"]}
                ]
            })
            
            # 📊 Summary
            UI.alert({
                type: "info"
                message: "📊 Showing {length(todos)} tasks"
            })
            
            # 📋 Todo list
            render_todo_list(todos)
        ]
    })
}

function create_todo() {
    # 📝 Create new todo from form data
    todo_data ← request.body()
    
    # ✅ Validation (visual validation flow)
    validation ← Validation.validate(todo_data, {
        title: {
            required: true
            min_length: 3
            max_length: 100
            message: "📝 Title must be 3-100 characters"
        }
        priority: {
            in: ["low", "medium", "high"]
            message: "🎯 Priority must be low, medium, or high"
        }
    })
    
    if NOT validation.valid {
        return UI.page({
            title: "❌ Validation Error"
            content: [
                UI.alert({
                    type: "danger"
                    message: "❌ Please fix the following issues:"
                })
                UI.validation_errors(validation.errors)
                UI.back_button()
            ]
        })
    }
    
    # 💾 Insert todo
    todo ← {
        title: todo_data.title
        description: todo_data.description or ""
        status: "pending"
        priority: todo_data.priority
        due_date: todo_data.due_date or null
        tags: "[]"  # Empty JSON array
    }
    
    result ← todo_db.insert("todos", todo)
    
    if result.success {
        # ✅ Success with clear feedback
        return UI.redirect("/todos", {
            success: "✅ Task '{todo.title}' created successfully!"
        })
    } else {
        # ❌ Error handling
        return UI.page({
            title: "❌ Error"
            content: [
                UI.alert({
                    type: "danger"
                    message: "❌ Failed to create task: {result.error}"
                })
                UI.back_button()
            ]
        })
    }
}

function update_todo(id) {
    # ✏️ Update existing todo
    todo ← todo_db.find("todos", {id: id})
    
    if NOT todo {
        return UI.page({
            title: "❌ Not Found"
            content: [
                UI.alert({
                    type: "danger"
                    message: "❌ Task not found"
                })
                UI.back_button()
            ]
        })
    }
    
    update_data ← request.body()
    
    # 🔄 Handle status toggle
    if update_data.action == "toggle_status" {
        new_status ← todo.status == "completed" ? "pending" : "completed"
        completed_at ← new_status == "completed" ? DateTime.now() : null
        
        result ← todo_db.update("todos", {id: id}, {
            status: new_status
            completed_at: completed_at
        })
        
        if result.success {
            message ← new_status == "completed" ? 
                "✅ Task marked as completed!" : 
                "📋 Task marked as pending!"
            
            return UI.redirect("/todos", {success: message})
        }
    }
    
    # 📝 Handle regular update
    result ← todo_db.update("todos", {id: id}, update_data)
    
    if result.success {
        return UI.redirect("/todos", {
            success: "✅ Task updated successfully!"
        })
    } else {
        return UI.page({
            title: "❌ Error"
            content: [
                UI.alert({
                    type: "danger"
                    message: "❌ Failed to update task: {result.error}"
                })
                UI.back_button()
            ]
        })
    }
}

function delete_todo(id) {
    # 🗑️ Delete todo
    todo ← todo_db.find("todos", {id: id})
    
    if NOT todo {
        return UI.redirect("/todos", {
            error: "❌ Task not found"
        })
    }
    
    result ← todo_db.delete("todos", {id: id})
    
    if result.success {
        return UI.redirect("/todos", {
            success: "✅ Task '{todo.title}' deleted successfully!"
        })
    } else {
        return UI.redirect("/todos", {
            error: "❌ Failed to delete task"
        })
    }
}

# 🎨 Helper Functions

function render_todo_list(todos) {
    # 📋 Render todos with visual clarity
    if length(todos) == 0 {
        return UI.empty_state({
            icon: "📝"
            title: "No tasks yet"
            description: "Start by adding your first task above!"
        })
    }
    
    return UI.list({
        items: todos.map(render_todo_item)
        class: "todo-list"
    })
}

function render_todo_item(todo) {
    # 🎨 Render individual todo with visual status
    status_icon ← todo.status == "completed" ? "✅" : "⏳"
    priority_color ← {
        "low": "green"
        "medium": "yellow" 
        "high": "red"
    }[todo.priority]
    
    return UI.card({
        class: "todo-item {todo.status}"
        content: [
            UI.grid([
                # 📊 Status and priority
                UI.badge({
                    text: "{status_icon} {todo.status}"
                    color: todo.status == "completed" ? "success" : "primary"
                })
                UI.badge({
                    text: "🎯 {todo.priority}"
                    color: priority_color
                })
            ])
            
            # 📝 Title and description
            UI.header(todo.title, level: 3)
            if todo.description {
                UI.paragraph(todo.description)
            }
            
            # 📅 Due date
            if todo.due_date {
                UI.paragraph("📅 Due: {todo.due_date}")
            }
            
            # 🎯 Action buttons
            UI.button_group([
                UI.button({
                    text: todo.status == "completed" ? "↩️ Reopen" : "✅ Complete"
                    action: "/todos/{todo.id}"
                    method: "PUT"
                    data: {action: "toggle_status"}
                    style: todo.status == "completed" ? "secondary" : "success"
                })
                UI.button({
                    text: "✏️ Edit"
                    action: "/todos/{todo.id}/edit"
                    style: "primary"
                })
                UI.button({
                    text: "🗑️ Delete"
                    action: "/todos/{todo.id}"
                    method: "DELETE"
                    style: "danger"
                    confirm: "Are you sure you want to delete this task?"
                })
            ])
        ]
    })
}

function get_todo_statistics() {
    # 📊 Calculate todo statistics
    total ← todo_db.count("todos")
    completed ← todo_db.count("todos", {status: "completed"})
    pending ← todo_db.count("todos", {status: "pending"})
    high_priority ← todo_db.count("todos", {priority: "high"})
    
    return {
        total: total
        completed: completed
        pending: pending
        high_priority: high_priority
        completion_rate: total > 0 ? (completed / total * 100).round() : 0
    }
}

function get_all_todos() {
    # 📋 Get all todos with sorting
    return todo_db.query("SELECT * FROM todos ORDER BY created_at DESC")
}

function get_recent_todos(limit = 5) {
    # 📋 Get recent todos
    return todo_db.query(
        "SELECT * FROM todos ORDER BY created_at DESC LIMIT {limit}"
    )
}

# 🚀 Start the application
main() {
    print("🚀 Starting Todo Web App...")
    print("📍 App will be available at: http://localhost:3000")
    print("🧠 Features:")
    print("   ✅ Neurodivergent-friendly UI")
    print("   📊 Visual task management")
    print("   🎯 Priority-based organization")
    print("   📅 Due date tracking")
    
    todo_app.start()
    
    print("✅ Todo app is running! 🎉")
    print("💡 Open http://localhost:3000 to get started!")
}

# 🧠 Accessibility Features:
# - High contrast color scheme
# - Large, readable fonts
# - Clear visual indicators (icons, colors)
# - Predictable navigation patterns
# - Minimal animations to reduce distraction
# - Consistent error handling and feedback
# - Keyboard navigation support
