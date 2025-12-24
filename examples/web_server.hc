// web_server.hc - A simple web server in HyperCode

// Import the web server module
import { Server, Router } from 'hypercode/web'

// Create a new web server
const app = new Server()
const router = new Router()

// Sample data store
let todos = [
    { id: 1, task: 'Learn HyperCode', completed: false },
    { id: 2, task: 'Build an API', completed: false },
    { id: 3, task: 'Deploy to production', completed: false }
]

// Middleware for JSON parsing
app.use(Server.json())

// GET /api/todos - Get all todos
router.get('/todos', (req, res) => {
    res.json({
        success: true,
        data: todos
    })
})

// GET /api/todos/:id - Get a single todo
router.get('/todos/:id', (req, res) => {
    const id = parseInt(req.params.id)
    const todo = todos.find(t => t.id === id)
    
    if (!todo) {
        return res.status(404).json({
            success: false,
            error: 'Todo not found'
        })
    }
    
    res.json({
        success: true,
        data: todo
    })
})

// POST /api/todos - Create a new todo
router.post('/todos', (req, res) => {
    const { task } = req.body
    
    if (!task) {
        return res.status(400).json({
            success: false,
            error: 'Task is required'
        })
    }
    
    const newTodo = {
        id: todos.length + 1,
        task,
        completed: false
    }
    
    todos.push(newTodo)
    
    res.status(201).json({
        success: true,
        data: newTodo
    })
})

// Mount the router
app.use('/api', router)

// Serve static files from the public directory
app.static('public')

// Start the server
const PORT = 3000
app.listen(PORT, () => {
    console.log(`🚀 Server running at http://localhost:${PORT}`)
    console.log('Available routes:')
    console.log(`  GET    http://localhost:${PORT}/api/todos`)
    console.log(`  GET    http://localhost:${PORT}/api/todos/:id`)
    console.log(`  POST   http://localhost:${PORT}/api/todos`)
    console.log(`\nTry it with:`)
    console.log(`  curl http://localhost:${PORT}/api/todos`)
    console.log(`  curl -X POST -H "Content-Type: application/json" -d '{"task":"New task"}' http://localhost:${PORT}/api/todos`)
})
