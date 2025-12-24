# 🚀 HyperCode API Server Example
# A simple REST API server built with HyperCode's neurodivergent-friendly syntax

import { Server, Router, Database } from hypercode:web

# 🌐 API Server Configuration
api_server Server {
    name: "HyperCode API Demo"
    port: 8080
    host: "localhost"
    
    # 🧠 Neurodivergent-friendly: Clear visual structure
    routes: [
        # GET /api/users - Fetch all users
        GET /api/users => fetch_all_users()
        
        # POST /api/users - Create new user  
        POST /api/users => create_user()
        
        # GET /api/users/:id - Fetch specific user
        GET /api/users/[id] => fetch_user(id)
        
        # PUT /api/users/:id - Update user
        PUT /api/users/[id] => update_user(id)
        
        # DELETE /api/users/:id - Delete user
        DELETE /api/users/[id] => delete_user(id)
    ]
}

# 📊 Database Connection (visual syntax)
db_connection Database {
    type: "sqlite"
    path: "./users.db"
    
    # 🎯 Clear table structure
    tables: {
        users: {
            id: INTEGER PRIMARY_KEY
            name: TEXT NOT_NULL
            email: TEXT UNIQUE
            created_at: TIMESTAMP DEFAULT_NOW
        }
    }
}

# 🔧 Helper Functions with visual clarity

function fetch_all_users() {
    # 📋 Get all users from database
    users ← db_connection.query("SELECT * FROM users ORDER BY created_at DESC")
    
    # 🎨 Format response for neurodivergent clarity
    response ← {
        status: "success"
        data: users
        count: length(users)
        message: "✅ Retrieved all users successfully"
    }
    
    return response
}

function create_user() {
    # 📝 Extract user data from request
    user_data ← request.body()
    
    # ✅ Validate input (visual validation flow)
    if NOT user_data.name OR NOT user_data.email {
        return {
            status: "error"
            message: "❌ Name and email are required"
            code: 400
        }
    }
    
    # 💾 Insert new user
    result ← db_connection.insert("users", user_data)
    
    if result.success {
        return {
            status: "success"
            data: result.user
            message: "✅ User created successfully"
            code: 201
        }
    } else {
        return {
            status: "error"
            message: "❌ Failed to create user"
            error: result.error
            code: 500
        }
    }
}

function fetch_user(id) {
    # 🔍 Find user by ID
    user ← db_connection.find("users", {id: id})
    
    if user {
        return {
            status: "success"
            data: user
            message: "✅ User found"
        }
    } else {
        return {
            status: "error"
            message: "❌ User not found"
            code: 404
        }
    }
}

function update_user(id) {
    # 📝 Get update data
    update_data ← request.body()
    
    # 🔍 Check if user exists
    existing_user ← db_connection.find("users", {id: id})
    
    if NOT existing_user {
        return {
            status: "error"
            message: "❌ User not found"
            code: 404
        }
    }
    
    # ✏️ Update user
    result ← db_connection.update("users", {id: id}, update_data)
    
    if result.success {
        return {
            status: "success"
            data: result.user
            message: "✅ User updated successfully"
        }
    } else {
        return {
            status: "error"
            message: "❌ Failed to update user"
            error: result.error
            code: 500
        }
    }
}

function delete_user(id) {
    # 🔍 Check if user exists
    existing_user ← db_connection.find("users", {id: id})
    
    if NOT existing_user {
        return {
            status: "error"
            message: "❌ User not found"
            code: 404
        }
    }
    
    # 🗑️ Delete user
    result ← db_connection.delete("users", {id: id})
    
    if result.success {
        return {
            status: "success"
            message: "✅ User deleted successfully"
        }
    } else {
        return {
            status: "error"
            message: "❌ Failed to delete user"
            error: result.error
            code: 500
        }
    }
}

# 🚀 Start the server
main() {
    print("🚀 Starting HyperCode API Server...")
    print("📍 Server will be available at: http://localhost:8080")
    print("📚 API Documentation:")
    print("   GET    /api/users     - List all users")
    print("   POST   /api/users     - Create new user")
    print("   GET    /api/users/:id - Get specific user")
    print("   PUT    /api/users/:id - Update user")
    print("   DELETE /api/users/:id - Delete user")
    
    # 🎯 Start server with visual feedback
    api_server.start()
    
    print("✅ Server is running! 🎉")
    print("💡 Try: curl http://localhost:8080/api/users")
}

# 🧠 Accessibility Features:
# - Clear visual structure with emojis
# - Consistent error handling patterns
# - Self-documenting code with visual cues
# - Predictable response formats
# - Color-coded status indicators (✅/❌)
