// task_manager.hc - A simple CLI task manager in HyperCode

// Define a Task type
type Task {
    id: number
    title: string
    completed: boolean
    priority: 'low' | 'medium' | 'high'
}

class TaskManager {
    tasks: Task[] = []
    nextId: number = 1

    // Add a new task
    function addTask(title: string, priority: 'low' | 'medium' | 'high' = 'medium'): Task {
        const task: Task = {
            id: this.nextId++,
            title,
            completed: false,
            priority
        }
        this.tasks.push(task)
        return task
    }

    // Mark a task as complete
    function completeTask(id: number): void {
        const task = this.tasks.find(t => t.id === id)
        if (task) {
            task.completed = true
        }
    }

    // List all tasks
    function listTasks(filter?: 'all' | 'active' | 'completed'): void {
        console.log("\n📋 Your Tasks")
        console.log("-".repeat(30))
        
        const filteredTasks = this.tasks.filter(task => {
            if (filter === 'active') return !task.completed
            if (filter === 'completed') return task.completed
            return true
        })

        if (filteredTasks.length === 0) {
            console.log("No tasks found!")
            return
        }

        for (const task of filteredTasks) {
            const status = task.completed ? '✅' : '⬜'
            console.log(`${status} [${task.priority[0].toUpperCase()}] #${task.id}: ${task.title}`)
        }
    }
}

// Example usage
function main() {
    console.log("🌟 Welcome to HyperCode Task Manager!")
    
    const taskManager = new TaskManager()
    
    // Add some sample tasks
    taskManager.addTask("Learn HyperCode basics", "high")
    taskManager.addTask("Create a sample project", "medium")
    taskManager.addTask("Read HyperCode documentation", "low")
    
    // Mark one as complete
    taskManager.completeTask(1)
    
    // Display all tasks
    taskManager.listTasks()
    
    console.log("\n✅ Task manager is working!")
}

// Run the example
main()
