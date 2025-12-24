# 🗄️ Database Integration Example
# Demonstrates HyperCode's neurodivergent-friendly database operations

import { Database, QueryBuilder, ORM } from hypercode:data
import { Validation, Encryption, Logger } from hypercode:utils
import { DateTime, UUID } from hypercode:core

# 🗄️ Database Configuration
app_db Database {
    # 🎯 Connection settings (visual clarity)
    connection: {
        type: "postgresql"
        host: "localhost"
        port: 5432
        database: "hypercode_app"
        username: "app_user"
        password: env("DB_PASSWORD")  # Secure environment variable
        
        # 🧠 Accessibility: Clear connection status
        pool_size: 10
        timeout: 30
        retry_attempts: 3
    }
    
    # 📊 Schema definition (visual structure)
    schema: {
        # 👥 Users table
        users: {
            id: UUID PRIMARY_KEY DEFAULT_GENERATE
            email: TEXT UNIQUE NOT_NULL
            username: TEXT UNIQUE NOT_NULL
            password_hash: TEXT NOT_NULL
            first_name: TEXT
            last_name: TEXT
            created_at: TIMESTAMP DEFAULT_NOW
            updated_at: TIMESTAMP DEFAULT_NOW
            last_login: TIMESTAMP NULL
            is_active: BOOLEAN DEFAULT_TRUE
            profile: JSON  # User preferences, settings
        }
        
        # 📝 Posts table
        posts: {
            id: UUID PRIMARY_KEY DEFAULT_GENERATE
            user_id: UUID REFERENCES users(id) ON_DELETE_CASCADE
            title: TEXT NOT_NULL
            content: TEXT NOT_NULL
            slug: TEXT UNIQUE NOT_NULL
            status: TEXT DEFAULT "draft"  # draft, published, archived
            published_at: TIMESTAMP NULL
            created_at: TIMESTAMP DEFAULT_NOW
            updated_at: TIMESTAMP DEFAULT_NOW
            tags: ARRAY[TEXT] DEFAULT "{}"
            metadata: JSON  # SEO, analytics data
        }
        
        # 💬 Comments table
        comments: {
            id: UUID PRIMARY_KEY DEFAULT_GENERATE
            post_id: UUID REFERENCES posts(id) ON_DELETE_CASCADE
            user_id: UUID REFERENCES users(id) ON_DELETE_CASCADE
            content: TEXT NOT_NULL
            parent_id: UUID NULL REFERENCES comments(id) ON_DELETE_CASCADE
            status: TEXT DEFAULT "published"  # published, hidden, deleted
            created_at: TIMESTAMP DEFAULT_NOW
            updated_at: TIMESTAMP DEFAULT_NOW
        }
        
        # 🏷️ Categories table
        categories: {
            id: UUID PRIMARY_KEY DEFAULT_GENERATE
            name: TEXT UNIQUE NOT_NULL
            slug: TEXT UNIQUE NOT_NULL
            description: TEXT
            color: TEXT DEFAULT "#2563eb"  # For UI theming
            created_at: TIMESTAMP DEFAULT_NOW
        }
        
        # 🔗 Post-Category junction table
        post_categories: {
            post_id: UUID REFERENCES posts(id) ON_DELETE_CASCADE
            category_id: UUID REFERENCES categories(id) ON_DELETE_CASCADE
            created_at: TIMESTAMP DEFAULT_NOW
            PRIMARY_KEY: (post_id, category_id)
        }
    }
    
    # 🧠 Migrations (visual version control)
    migrations: {
        version: "1.0.0"
        auto_migrate: true
        rollback_on_error: false
    }
}

# 🎯 ORM Models (visual object mapping)

model User {
    table: "users"
    
    # 📝 Fields with validation
    fields: {
        id: UUID PRIMARY_KEY
        email: {
            type: TEXT
            validation: {
                required: true
                email: true
                unique: true
                message: "📧 Please enter a valid email address"
            }
        }
        username: {
            type: TEXT
            validation: {
                required: true
                min_length: 3
                max_length: 30
                pattern: "^[a-zA-Z0-9_]+$"
                message: "👤 Username must be 3-30 characters, letters/numbers/underscores only"
            }
        }
        password_hash: {
            type: TEXT
            validation: {
                required: true
                min_length: 60  # bcrypt hash length
                message: "🔒 Invalid password hash"
            }
        }
        first_name: {
            type: TEXT
            validation: {
                max_length: 50
                message: "📝 First name too long"
            }
        }
        last_name: {
            type: TEXT
            validation: {
                max_length: 50
                message: "📝 Last name too long"
            }
        }
        is_active: {
            type: BOOLEAN
            default: true
        }
        profile: {
            type: JSON
            default: "{}"
        }
    }
    
    # 🔍 Relationships (visual connections)
    relationships: {
        posts: {
            type: "has_many"
            model: "Post"
            foreign_key: "user_id"
            cascade_delete: true
        }
        comments: {
            type: "has_many"
            model: "Comment"
            foreign_key: "user_id"
            cascade_delete: true
        }
    }
    
    # 🎯 Methods (business logic)
    methods: {
        # 🔐 Authentication
        authenticate(password) {
            # 🧠 Clear authentication flow
            if NOT this.is_active {
                return {
                    success: false
                    message: "❌ Account is deactivated"
                }
            }
            
            # 🔒 Verify password
            password_valid ← Encryption.verify(password, this.password_hash)
            
            if password_valid {
                # 📝 Update last login
                this.update({last_login: DateTime.now()})
                
                return {
                    success: true
                    message: "✅ Authentication successful"
                    user: this.sanitize()  # Remove sensitive data
                }
            } else {
                return {
                    success: false
                    message: "❌ Invalid password"
                }
            }
        }
        
        # 🧹 Sanitize user data (remove sensitive info)
        sanitize() {
            return {
                id: this.id
                email: this.email
                username: this.username
                first_name: this.first_name
                last_name: this.last_name
                created_at: this.created_at
                last_login: this.last_login
                profile: this.profile
            }
        }
        
        # 📝 Update profile
        update_profile(profile_data) {
            # ✅ Validate profile data
            validation ← Validation.validate(profile_data, {
                bio: {max_length: 500}
                website: {url: true}
                location: {max_length: 100}
                theme: {in: ["light", "dark", "auto"]}
            })
            
            if NOT validation.valid {
                return {
                    success: false
                    message: "❌ Invalid profile data"
                    errors: validation.errors
                }
            }
            
            # 💾 Update profile
            result ← this.update({
                profile: merge(this.profile, profile_data)
            })
            
            return result
        }
    }
}

model Post {
    table: "posts"
    
    # 📝 Fields
    fields: {
        id: UUID PRIMARY_KEY
        user_id: UUID REFERENCES users(id)
        title: {
            type: TEXT
            validation: {
                required: true
                min_length: 5
                max_length: 200
                message: "📝 Title must be 5-200 characters"
            }
        }
        content: {
            type: TEXT
            validation: {
                required: true
                min_length: 10
                message: "📄 Content must be at least 10 characters"
            }
        }
        slug: {
            type: TEXT
            validation: {
                required: true
                unique: true
                pattern: "^[a-z0-9-]+$"
                message: "🔗 Slug must contain only lowercase letters, numbers, and hyphens"
            }
        }
        status: {
            type: TEXT
            validation: {
                in: ["draft", "published", "archived"]
                message: "📊 Status must be draft, published, or archived"
            }
            default: "draft"
        }
        tags: {
            type: ARRAY[TEXT]
            default: "{}"
        }
    }
    
    # 🔍 Relationships
    relationships: {
        author: {
            type: "belongs_to"
            model: "User"
            foreign_key: "user_id"
        }
        comments: {
            type: "has_many"
            model: "Comment"
            foreign_key: "post_id"
            cascade_delete: true
        }
        categories: {
            type: "has_many"
            through: "post_categories"
            model: "Category"
        }
    }
    
    # 🎯 Methods
    methods: {
        # 📖 Publish post
        publish() {
            if this.status == "published" {
                return {
                    success: false
                    message: "❌ Post is already published"
                }
            }
            
            result ← this.update({
                status: "published"
                published_at: DateTime.now()
            })
            
            if result.success {
                # 📝 Log publication
                Logger.info("Post published", {
                    post_id: this.id
                    title: this.title
                    user_id: this.user_id
                })
            }
            
            return result
        }
        
        # 🏷️ Add category
        add_category(category_id) {
            # 🔍 Check if category exists
            category ← Category.find(category_id)
            if NOT category {
                return {
                    success: false
                    message: "❌ Category not found"
                }
            }
            
            # 🔗 Create junction record
            result ← app_db.insert("post_categories", {
                post_id: this.id
                category_id: category_id
            })
            
            return result
        }
        
        # 📊 Get statistics
        get_stats() {
            comment_count ← Comment.where("post_id = ?", [this.id]).count()
            
            return {
                comments: comment_count
                views: this.metadata.views or 0
                likes: this.metadata.likes or 0
                word_count: length(split(this.content, " "))
                reading_time: ceil(length(split(this.content, " ")) / 200)  # 200 wpm
            }
        }
    }
}

# 🔧 Database Operations Examples

function create_user_example() {
    # 👤 Create new user with validation
    user_data ← {
        email: "user@example.com"
        username: "newuser123"
        password: "secure_password_123"
        first_name: "John"
        last_name: "Doe"
        profile: {
            bio: "Passionate developer and HyperCode enthusiast"
            website: "https://example.com"
            location: "San Francisco, CA"
            theme: "dark"
        }
    }
    
    # ✅ Validate user data
    validation ← Validation.validate(user_data, {
        email: {required: true, email: true}
        username: {required: true, min_length: 3}
        password: {required: true, min_length: 8}
    })
    
    if NOT validation.valid {
        return {
            success: false
            message: "❌ Validation failed"
            errors: validation.errors
        }
    }
    
    # 🔒 Hash password
    password_hash ← Encryption.hash(user_data.password)
    
    # 👤 Create user
    user ← User.create({
        email: user_data.email
        username: user_data.username
        password_hash: password_hash
        first_name: user_data.first_name
        last_name: user_data.last_name
        profile: user_data.profile
    })
    
    if user.success {
        Logger.info("User created", {
            user_id: user.data.id
            username: user.data.username
        })
        
        return {
            success: true
            message: "✅ User created successfully"
            user: user.data.sanitize()
        }
    } else {
        return {
            success: false
            message: "❌ Failed to create user"
            error: user.error
        }
    }
}

function create_blog_post_example() {
    # 📝 Create blog post with categories
    post_data ← {
        user_id: "550e8400-e29b-41d4-a716-446655440000"  # Example user ID
        title: "Getting Started with HyperCode"
        content: "HyperCode is a revolutionary programming language designed with neurodivergent developers in mind. Its visual syntax and clear structure make coding more accessible and enjoyable..."
        slug: "getting-started-with-hypercode"
        tags: ["hypercode", "programming", "neurodiversity", "tutorial"]
        status: "draft"
    }
    
    # 📝 Create post
    post ← Post.create(post_data)
    
    if post.success {
        # 🏷️ Add categories
        categories ← ["programming", "tutorials"]
        
        for category_name in categories {
            category ← Category.where("slug = ?", [category_name]).first()
            if category {
                post.data.add_category(category.id)
            }
        }
        
        # 📊 Get post statistics
        stats ← post.data.get_stats()
        
        return {
            success: true
            message: "✅ Post created successfully"
            post: post.data
            stats: stats
        }
    } else {
        return {
            success: false
            message: "❌ Failed to create post"
            error: post.error
        }
    }
}

function complex_query_example() {
    # 🔍 Complex query with joins and aggregations
    
    # 📊 Get posts with author info and comment counts
    popular_posts ← QueryBuilder.select({
        # 📝 Post fields
        "p.id": "post_id"
        "p.title": "title"
        "p.slug": "slug"
        "p.published_at": "published_at"
        
        # 👤 Author fields
        "u.username": "author_username"
        "u.first_name": "author_first_name"
        "u.last_name": "author_last_name"
        
        # 💬 Comment count
        "COUNT(c.id)": "comment_count"
        
        # 🏷️ Category names
        "ARRAY_AGG(cat.name)": "categories"
    })
    .from("posts", "p")
    .join("users", "u", "p.user_id = u.id")
    .left_join("comments", "c", "p.id = c.post_id AND c.status = 'published'")
    .left_join("post_categories", "pc", "p.id = pc.post_id")
    .left_join("categories", "cat", "pc.category_id = cat.id")
    .where("p.status = ?", ["published"])
    .where("p.published_at >= ?", [DateTime.now().subtract(days: 30)])
    .group_by("p.id, u.id")
    .order_by("comment_count DESC")
    .limit(10)
    .execute()
    
    return popular_posts
}

function transaction_example() {
    # 🔄 Transaction example for complex operations
    
    result ← app_db.transaction(function(tx) {
        # 👤 Create user
        user ← tx.insert("users", {
            email: "transaction@example.com"
            username: "tx_user"
            password_hash: Encryption.hash("password123")
        })
        
        if NOT user.success {
            tx.rollback()
            return {success: false, message: "❌ Failed to create user"}
        }
        
        # 📝 Create welcome post
        post ← tx.insert("posts", {
            user_id: user.data.id
            title: "My First Post"
            content: "Hello, HyperCode world!"
            slug: "my-first-post"
            status: "published"
            published_at: DateTime.now()
        })
        
        if NOT post.success {
            tx.rollback()
            return {success: false, message: "❌ Failed to create post"}
        }
        
        # ✅ Commit transaction
        tx.commit()
        
        return {
            success: true
            message: "✅ User and post created successfully"
            user: user.data
            post: post.data
        }
    })
    
    return result
}

# 🚀 Main application
main() {
    print("🗄️ Database Integration Example")
    print("📍 Demonstrating HyperCode's database capabilities")
    print("🧠 Features:")
    print("   🎯 Visual schema definition")
    print("   🔍 ORM with relationships")
    print("   ✅ Built-in validation")
    print("   🔄 Transaction support")
    print("   🔒 Security and encryption")
    print("   📊 Complex queries")
    
    # 🗄️ Initialize database
    if app_db.connect() {
        print("✅ Database connected successfully!")
        
        # 🔄 Run migrations
        app_db.migrate()
        
        # 👤 Create sample user
        user_result ← create_user_example()
        print(user_result.message)
        
        # 📝 Create sample post
        post_result ← create_blog_post_example()
        print(post_result.message)
        
        # 🔍 Run complex query
        posts ← complex_query_example()
        print("📊 Found {length(posts)} popular posts")
        
        # 🔄 Test transaction
        tx_result ← transaction_example()
        print(tx_result.message)
        
        print("✅ Database examples completed! 🎉")
    } else {
        print("❌ Failed to connect to database")
    }
}

# 🧠 Accessibility Features:
# - Clear visual structure with emojis
# - Consistent error handling patterns
# - Self-documenting code
# - Predictable response formats
# - Visual validation feedback
# - Color-coded status indicators
