// TaskManager.hc - A simple task manager in HyperCode

// Define a Task type
type Task {
    id: string
    title: string
    completed: boolean
    priority: 'low' | 'medium' | 'high'
    dueDate: Date | null
}

// Task manager class
class TaskManager {
    tasks: Task[] = []
    
    // Add a new task
    function addTask(title: string, priority: 'low' | 'medium' | 'high' = 'medium'): Task {
        const newTask: Task = {
            id: generateId(),
            title,
            completed: false,
            priority,
            dueDate: null
        }
        this.tasks.push(newTask)
        return newTask
    }
    
    // Mark a task as complete
    function completeTask(taskId: string): void {
        const task = this.tasks.find(t => t.id === taskId)
        if (task) {
            task.completed = true
        }
    }
    
    // Get tasks by priority
    function getTasksByPriority(priority: 'low' | 'medium' | 'high'): Task[] {
        return this.tasks.filter(task => task.priority === priority)
    }
    
    // Helper function to generate a unique ID
    private function generateId(): string {
        return Math.random().toString(36).substr(2, 9)
    }
}

// Example usage
function main() {
    // Create a new task manager
    const taskManager = new TaskManager()
    
    // Add some tasks
    taskManager.addTask('Learn HyperCode', 'high')
    taskManager.addTask('Build a sample app', 'medium')
    taskManager.addTask('Write documentation', 'low')
    
    // Complete a task
    if (taskManager.tasks.length > 0) {
        taskManager.completeTask(taskManager.tasks[0].id)
    }
    
    // Print all tasks
    console.log('All tasks:')
    for (const task of taskManager.tasks) {
        console.log(`- [${task.completed ? 'x' : ' '}] ${task.title} (${task.priority})`)
    }
    
    // Get high priority tasks
    const highPriorityTasks = taskManager.getTasksByPriority('high')
    console.log('\nHigh priority tasks:')
    for (const task of highPriorityTasks) {
        console.log(`- ${task.title}`)
    }
}

// Run the example
main()
