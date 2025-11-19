# 🎨 HyperCode Style Guide (Draft)

> **🧠 Neurodivergent-First Design** - This style guide prioritizes cognitive accessibility, visual clarity, and reduced mental load for all developers, especially neurodivergent individuals.

## 🎯 Guiding Principles

### 🧠 **Accessibility First**
- **Visual patterns** reduce cognitive load
- **Consistent structure** improves predictability
- **Clear indicators** aid code navigation
- **Minimal distractions** maintain focus

### 🎨 **Visual Clarity**
- **Emoji indicators** for quick recognition
- **Color-coded comments** for different purposes
- **Consistent spacing** for visual grouping
- **Logical organization** for easy scanning

### 📊 **Predictability**
- **Standardized patterns** across codebases
- **Consistent naming** conventions
- **Regular structure** in functions and files
- **Clear error handling** patterns

---

## 📝 Code Formatting

### 📏 **Line Length**
- **Maximum 100 characters** per line
- **Break long expressions** across multiple lines
- **Align continuation lines** for visual clarity

```hypercode
# ✅ Good - Clear line breaks
user_data ← User.find_by_email_and_status(
    email: user_email,
    status: "active",
    include_deleted: false
)

# ❌ Avoid - Too long
user_data ← User.find_by_email_and_status(email: user_email, status: "active", include_deleted: false)
```

### 📐 **Indentation**
- **4 spaces** for indentation (no tabs)
- **Consistent alignment** for multi-line statements
- **Visual grouping** with indentation levels

```hypercode
# ✅ Good - Consistent 4-space indentation
function process_user_data(user_info) {
    # 🧠 Validate input
    if NOT user_info.email {
        return {success: false, message: "❌ Email required"}
    }
    
    # 🔍 Find existing user
    existing_user ← User.where("email = ?", [user_info.email]).first()
    
    if existing_user {
        # 📝 Update user
        result ← existing_user.update(user_info)
    } else {
        # 👤 Create new user
        result ← User.create(user_info)
    }
    
    return result
}
```

### 📄 **Spacing**
- **Single blank line** between logical sections
- **Two blank lines** between major functions
- **No trailing spaces** at end of lines
- **Space around operators** for readability

```hypercode
# ✅ Good - Clear spacing
total ← price + tax + shipping
discount ← total * discount_rate
final_price ← total - discount

# ❌ Avoid - Cramped spacing
total←price+tax+shipping
discount←total*discount_rate
```

---

## 🏷️ Naming Conventions

### 📦 **Variables**
- **snake_case** for all variables
- **Descriptive names** that indicate purpose
- **Prefix indicators** for special variables

```hypercode
# ✅ Good - Clear, descriptive names
user_email ← "user@example.com"
is_authenticated ← true
temp_user_data ← {...}
active_session_count ← 42

# ❌ Avoid - Unclear names
e ← "user@example.com"
auth ← true
data ← {...}
count ← 42
```

### 🔧 **Functions**
- **snake_case** with action verbs
- **Clear purpose** in the name
- **Consistent patterns** for similar operations

```hypercode
# ✅ Good - Action-oriented names
get_user_by_id(user_id)
create_new_user(user_data)
validate_email_format(email)
calculate_total_price(items)

# ❌ Avoid - Unclear purposes
user(id)
make(data)
check(email)
total(items)
```

### 🏗️ **Classes/Structures**
- **PascalCase** for types
- **Descriptive names** that indicate structure
- **Clear purpose** in the name

```hypercode
# ✅ Good - Clear type names
UserData ← {...}
ApiResponse ← {...}
DatabaseConnection ← {...}

# ❌ Avoid - Unclear types
Data ← {...}
Response ← {...}
Connection ← {...}
```

---

## 💬 Comment Style

### 🎨 **Comment Categories**
- **🧠 Cognitive notes** - Explain mental models
- **📝 Function descriptions** - Document purpose
- **⚠️ Warnings** - Highlight potential issues
- **💡 Tips** - Share helpful insights
- **🔧 Implementation notes** - Technical details

```hypercode
# 🧠 This function processes user authentication
# It follows a clear mental model: validate → check → authenticate → return

function authenticate_user(credentials) {
    # 📝 Validate input format
    if NOT credentials.email OR NOT credentials.password {
        return {success: false, message: "❌ Email and password required"}
    }
    
    # 🔍 Find user by email
    user ← User.where("email = ?", [credentials.email]).first()
    
    if NOT user {
        return {success: false, message: "❌ User not found"}
    }
    
    # ⚠️ Rate limiting check
    if is_rate_limited(user.id) {
        return {success: false, message: "⏰ Too many attempts, try again later"}
    }
    
    # 🔐 Verify password
    password_valid ← Encryption.verify(credentials.password, user.password_hash)
    
    if password_valid {
        # 💡 Update last login for analytics
        user.update({last_login: DateTime.now()})
        
        return {
            success: true,
            message: "✅ Authentication successful",
            user: user.sanitize()
        }
    } else {
        return {success: false, message: "❌ Invalid password"}
    }
}
```

### 📊 **Comment Density**
- **Moderate comments** - Not too sparse, not too dense
- **Purposeful comments** - Add value, don't restate code
- **Visual separation** - Comments should enhance readability

```hypercode
# ✅ Good - Purposeful comments
function calculate_discount(price, user_level) {
    # 📊 Discount rates by user level
    discount_rates ← {
        "bronze": 0.05
        "silver": 0.10
        "gold": 0.15
        "platinum": 0.20
    }
    
    # 🔍 Get applicable rate
    rate ← discount_rates[user_level] or 0.0
    
    # 💰 Calculate final price
    discounted_price ← price * (1 - rate)
    
    return discounted_price
}

# ❌ Avoid - Unhelpful comments
function calculate_discount(price, user_level) {
    # Define discount rates
    discount_rates ← {...}
    
    # Get the rate
    rate ← discount_rates[user_level] or 0.0
    
    # Calculate the price
    discounted_price ← price * (1 - rate)
    
    return discounted_price
}
```

---

## 🎯 Structure Patterns

### 📁 **File Organization**
```
project_name.hc
├── 📋 Header with description
├── 📦 Import statements
├── ⚙️ Configuration section
├── 🔧 Core functionality
├── 🎨 Helper functions
├── 🧪 Test functions (if applicable)
└── 🚀 Main entry point
```

### 🏗️ **Function Structure**
```hypercode
# 📝 Function description (what and why)
function function_name(parameters) {
    # 🧠 Mental model/explanation (if complex)
    
    # 📋 Input validation
    if NOT validate_inputs(parameters) {
        return error_response
    }
    
    # 🔍 Main logic (clear steps)
    step_1_result ← perform_step_1()
    step_2_result ← perform_step_2(step_1_result)
    final_result ← perform_step_3(step_2_result)
    
    # ✅ Success response
    return {
        success: true
        data: final_result
        message: "✅ Operation completed"
    }
}
```

### 📊 **Error Handling Patterns**
```hypercode
# 🎯 Consistent error response format
{
    success: false
    message: "❌ Clear, actionable error message"
    error_code: "SPECIFIC_ERROR_CODE"
    details: {...}  # Optional additional context
}

# ✅ Consistent success response format
{
    success: true
    message: "✅ Clear success message"
    data: {...}  # Main result
    metadata: {...}  # Optional additional info
}
```

---

## 🎨 Visual Patterns

### 🎯 **Emoji Usage**
- **🧠** - Cognitive notes, mental models
- **📝** - Documentation, descriptions
- **🔍** - Search, lookup, validation
- **✅** - Success, completion
- **❌** - Errors, failures
- **⚠️** - Warnings, cautions
- **💡** - Tips, insights
- **🔧** - Implementation, technical details
- **🚀** - Entry points, main functions
- **📊** - Data, metrics, calculations

### 🌈 **Color Coding (in comments)**
```hypercode
# 🧠 Blue - Cognitive explanations
# 📝 Green - Documentation
# ⚠️ Yellow - Warnings
# ❌ Red - Errors
# 💡 Purple - Tips and insights
```

### 📐 **Visual Grouping**
```hypercode
# 📊 Data Processing Section
# -------------------------

# 🔍 Input validation
validate_data()

# 📝 Data transformation
transform_data()

# 💾 Data storage
save_data()


# 🎨 UI Rendering Section
# ----------------------

# 🖼️ Component creation
create_components()

# 🎯 Event handling
setup_events()

# 📱 Layout management
arrange_layout()
```

---

## 🧪 Testing Patterns

### 📝 **Test Naming**
- **test_[function]_[scenario]** format
- **Descriptive scenarios** that indicate what's being tested
- **Consistent patterns** for similar test types

```hypercode
# ✅ Good test names
test_authenticate_user_valid_credentials()
test_authenticate_user_invalid_password()
test_authenticate_user_nonexistent_user()

# ❌ Avoid unclear names
test_auth_1()
test_auth_2()
test_auth_bad()
```

### 🏗️ **Test Structure**
```hypercode
# 📝 Test description
function test_function_scenario() {
    # 🧠 Arrange - Set up test data
    test_data ← create_test_data()
    
    # 🔧 Act - Execute function being tested
    result ← function_being_tested(test_data)
    
    # ✅ Assert - Verify expected outcome
    assert(result.success == true)
    assert(result.data == expected_data)
}
```

---

## 🔧 Implementation Guidelines

### 📊 **Data Structures**
- **Clear field names** that indicate purpose
- **Consistent types** across similar structures
- **Documentation** for complex nested structures

```hypercode
# ✅ Good - Clear data structure
User ← {
    id: UUID
    email: TEXT
    username: TEXT
    profile: {
        bio: TEXT
        preferences: {
            theme: TEXT  # "light", "dark", "auto"
            notifications: BOOLEAN
        }
    }
}

# ❌ Avoid - Unclear structure
User ← {
    id: UUID
    e: TEXT
    u: TEXT
    p: {
        b: TEXT
        prefs: {
            t: TEXT
            n: BOOLEAN
        }
    }
}
```

### 🔍 **Database Operations**
- **Descriptive query names**
- **Clear parameter naming**
- **Consistent error handling**

```hypercode
# ✅ Good - Clear database operations
function get_active_users_by_department(department_id) {
    query ← """
        SELECT id, email, username
        FROM users
        WHERE department_id = ?
        AND is_active = true
        ORDER BY username
    """
    
    results ← Database.query(query, [department_id])
    
    return {
        success: true
        data: results
        count: length(results)
    }
}
```

---

## 📚 Documentation Standards

### 📖 **Function Documentation**
```hypercode
# 📝 Calculate total price with discounts and taxes
# 
# 🎯 Purpose: Compute final price including all applicable charges
# 🧠 Mental Model: Base Price → Apply Discounts → Add Tax → Add Shipping
#
# 📋 Parameters:
#   - base_price: Numeric value of the item
#   - discount_code: Optional discount identifier
#   - user_level: Customer tier ("bronze", "silver", "gold", "platinum")
#   - shipping_method: Delivery speed ("standard", "express", "overnight")
#
# ✅ Returns: Object with final price and breakdown
# ❌ Errors: Invalid parameters, unavailable shipping
#
# 💡 Example: calculate_final_price(100.00, "SAVE20", "gold", "express")
function calculate_final_price(base_price, discount_code, user_level, shipping_method) {
    # Implementation...
}
```

### 📁 **File Headers**
```hypercode
# 📋 [Project Name] - [Brief Description]
# 
# 🎯 Purpose: [What this file accomplishes]
# 🧠 Mental Model: [How to understand this file]
# 👤 Author: [Author name]
# 📅 Created: [Creation date]
# 🔄 Updated: [Last update date]
#
# 📚 Dependencies: [Required modules/packages]
# 🔗 Related Files: [Connected files/modules]
#
# 💡 Usage: [How to use this file]
```

---

## 🎯 Style Guide Evolution

### 📊 **Feedback Collection**
- **GitHub Issues** using the style feedback template
- **Community discussions** on Discord
- **User surveys** for accessibility preferences
- **Code reviews** for pattern consistency

### 🔄 **Review Process**
1. **Monthly review** of collected feedback
2. **Community voting** on major changes
3. **Accessibility testing** with neurodivergent users
4. **Gradual implementation** of approved changes

### 📈 **Metrics for Success**
- **Code consistency** across community projects
- **User satisfaction** with style guidelines
- **Accessibility compliance** scores
- **Adoption rate** of recommended patterns

---

## 🙏 Contributing to This Guide

This style guide is **community-driven** and **accessibility-focused**. Your feedback helps make HyperCode better for everyone, especially neurodivergent developers.

### 📝 **How to Contribute**
1. **Use the style feedback template** in GitHub Issues
2. **Join discussions** on Discord
3. **Share your examples** of good/bad patterns
4. **Test guidelines** with your own code

### 🧠 **Accessibility Focus**
- **Prioritize neurodivergent needs** in all suggestions
- **Test with assistive technologies**
- **Consider cognitive load** in all recommendations
- **Maintain visual clarity** as a core principle

---

## 📞 Get Help

- **📧 Email**: [style@hypercode.dev](mailto:style@hypercode.dev)
- **💬 Discord**: [HyperCode Community](https://discord.gg/hypercode)
- **🐛 Issues**: [GitHub Issues](https://github.com/welshDog/hypercode/issues)
- **💡 Discussions**: [GitHub Discussions](https://github.com/welshDog/hypercode/discussions)

---

**🎉 Together, we're building a more accessible programming future!**
