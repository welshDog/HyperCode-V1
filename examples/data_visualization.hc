# 📊 Data Visualization with HyperCode Spatial Visualizer
# Demonstrates HyperCode's visual syntax for data analysis and visualization

import { SpatialVisualizer, DataProcessor, Charts } from hypercode:spatial
import { Database, FileSystem } from hypercode:data
import { Math, Statistics } from hypercode:utils

# 🎨 Visualization Configuration
viz_config SpatialVisualizer {
    theme: "neurodivergent_friendly"
    colors: {
        primary: ["#2563eb", "#7c3aed", "#db2777", "#dc2626", "#ea580c", "#ca8a04", "#16a34a", "#0891b2"]
        background: "#ffffff"
        text: "#1f2937"
        grid: "#e5e7eb"
    }
    accessibility: {
        high_contrast: true
        color_blind_safe: true
        large_labels: true
        minimal_animations: true
    }
}

# 📊 Sample Data Sources
data_sources {
    # 📈 Sales data
    sales_data Database {
        type: "csv"
        path: "./data/sales.csv"
        
        schema: {
            date: DATE
            product: TEXT
            category: TEXT
            revenue: DECIMAL
            units: INTEGER
            region: TEXT
        }
    }
    
    # 👥 User analytics
    user_data Database {
        type: "json"
        path: "./data/users.json"
        
        schema: {
            user_id: INTEGER
            signup_date: DATE
            last_active: DATE
            sessions: INTEGER
            features_used: ARRAY
            subscription_type: TEXT
        }
    }
    
    # 🌐 Real-time data stream
    realtime_data DataProcessor {
        source: "https://api.example.com/metrics"
        refresh_interval: 30  # seconds
        format: "json"
    }
}

# 🎯 Main Visualization Dashboard
function create_dashboard() {
    # 📊 Load and process data
    sales ← sales_data.query("SELECT * FROM sales_data WHERE date >= date('now', '-30 days')")
    users ← user_data.load()
    realtime ← realtime_data.fetch()
    
    # 🎨 Create dashboard layout
    dashboard ← viz_config.dashboard({
        title: "📊 Business Analytics Dashboard"
        layout: "grid_2x2"
        auto_refresh: 30
        
        panels: [
            # 📈 Revenue Trend
            create_revenue_chart(sales)
            
            # 🏆 Top Products
            create_top_products_chart(sales)
            
            # 👥 User Growth
            create_user_growth_chart(users)
            
            # 🌍 Regional Performance
            create_regional_map(sales)
            
            # ⚡ Real-time Metrics
            create_realtime_panel(realtime)
            
            # 📋 Summary Stats
            create_summary_panel(sales, users)
        ]
    })
    
    return dashboard
}

# 📈 Revenue Trend Visualization
function create_revenue_chart(sales_data) {
    # 🔄 Process data
    daily_revenue ← sales_data.group_by("date")
        .aggregate({
            total_revenue: sum("revenue")
            total_units: sum("units")
        })
        .order_by("date")
    
    # 📊 Create line chart with visual clarity
    return viz_config.chart({
        type: "line"
        title: "📈 Revenue Trend (30 Days)"
        data: daily_revenue
        
        # 🎨 Visual configuration
        x_axis: {
            field: "date"
            label: "📅 Date"
            format: "MMM DD"
        }
        y_axis: {
            field: "total_revenue"
            label: "💰 Revenue ($)"
            format: "$#,##0"
        }
        
        # 🧠 Neurodivergent-friendly features
        series: [
            {
                name: "Revenue"
                color: "primary[0]"
                line_style: "solid"
                line_width: 3
                point_style: "circle"
                point_size: 4
                tooltip: "📅 {date}: ${total_revenue}"
            }
        ]
        
        # 📊 Additional metrics
        secondary_axis: {
            field: "total_units"
            label: "📦 Units Sold"
            chart_type: "bar"
            color: "primary[3]"
            opacity: 0.3
        }
        
        # 🎯 Statistical overlays
        overlays: [
            {
                type: "trend_line"
                color: "primary[1]"
                style: "dashed"
                label: "📈 Trend"
            }
            {
                type: "average"
                color: "primary[2]"
                style: "dotted"
                label: "📊 Average"
            }
        ]
        
        # 🧠 Accessibility
        accessibility: {
            alt_text: "Line chart showing revenue trend over 30 days with units sold as bars"
            keyboard_navigation: true
            high_contrast: true
        }
    })
}

# 🏆 Top Products Visualization
function create_top_products_chart(sales_data) {
    # 🔄 Aggregate product data
    product_stats ← sales_data.group_by("product", "category")
        .aggregate({
            total_revenue: sum("revenue")
            total_units: sum("units")
            avg_price: average("revenue" / "units")
        })
        .order_by("total_revenue")
        .limit(10)
    
    # 📊 Create horizontal bar chart
    return viz_config.chart({
        type: "bar"
        orientation: "horizontal"
        title: "🏆 Top 10 Products by Revenue"
        data: product_stats
        
        # 🎨 Visual configuration
        x_axis: {
            field: "total_revenue"
            label: "💰 Revenue ($)"
            format: "$#,##0"
        }
        y_axis: {
            field: "product"
            label: "📦 Product"
        }
        
        # 🎨 Color by category
        color_by: "category"
        color_scheme: "categorical"
        
        # 🧠 Interactive features
        interactions: [
            {
                type: "hover"
                action: "highlight_category"
            }
            {
                type: "click"
                action: "drill_down"
                target: "product_details"
            }
        ]
        
        # 📊 Data labels for clarity
        data_labels: {
            show: true
            format: "${total_revenue}"
            position: "outside"
            font_size: "medium"
        }
        
        # 🧠 Accessibility
        accessibility: {
            alt_text: "Horizontal bar chart showing top 10 products by revenue, colored by category"
            sortable: true
            filterable: true
        }
    })
}

# 👥 User Growth Visualization
function create_user_growth_chart(user_data) {
    # 🔄 Process user data
    user_growth ← user_data.group_by(format_date("signup_date", "YYYY-MM"))
        .aggregate({
            new_users: count("user_id")
            active_users: count_distinct("user_id", condition: "last_active >= date('now', '-30 days')")
        })
        .order_by("month")
    
    # 📊 Create area chart
    return viz_config.chart({
        type: "area"
        title: "👥 User Growth Over Time"
        data: user_growth
        
        # 🎨 Visual configuration
        x_axis: {
            field: "month"
            label: "📅 Month"
            format: "MMM YYYY"
        }
        y_axis: {
            field: "new_users"
            label: "👤 New Users"
            format: "#,##0"
        }
        
        # 🎨 Stacked areas
        series: [
            {
                name: "New Users"
                field: "new_users"
                color: "primary[0]"
                opacity: 0.8
            }
            {
                name: "Active Users"
                field: "active_users"
                color: "primary[2]"
                opacity: 0.6
            }
        ]
        
        # 📊 Growth indicators
        indicators: [
            {
                type: "growth_rate"
                period: "month_over_month"
                label: "📈 MoM Growth"
                format: "+#.#%"
            }
            {
                type: "total"
                label: "👥 Total Users"
                value: sum("new_users")
            }
        ]
        
        # 🧠 Accessibility
        accessibility: {
            alt_text: "Area chart showing user growth over time with new and active users"
            data_table_available: true
        }
    })
}

# 🌍 Regional Performance Map
function create_regional_map(sales_data) {
    # 🔄 Aggregate regional data
    regional_stats ← sales_data.group_by("region")
        .aggregate({
            total_revenue: sum("revenue")
            total_units: sum("units")
            avg_order_value: average("revenue")
        })
        .order_by("total_revenue")
    
    # 🗺️ Create geographic visualization
    return viz_config.map({
        type: "choropleth"
        title: "🌍 Regional Performance"
        data: regional_stats
        
        # 🗺️ Map configuration
        geography: "countries"
        field: "region"
        value_field: "total_revenue"
        
        # 🎨 Color scale
        color_scale: {
            type: "sequential"
            colors: "primary"
            reverse: false
        }
        
        # 📊 Tooltips
        tooltip: {
            title: "{region}"
            fields: [
                {label: "💰 Revenue", value: "${total_revenue}"}
                {label: "📦 Units", value: "{total_units}"}
                {label: "📊 Avg Order", value: "${avg_order_value}"}
            ]
        }
        
        # 🧠 Accessibility
        accessibility: {
            alt_text: "Map showing regional sales performance with color coding by revenue"
            keyboard_navigation: true
            high_contrast: true
        }
    })
}

# ⚡ Real-time Metrics Panel
function create_realtime_panel(realtime_data) {
    # 📊 Create real-time metrics display
    return viz_config.panel({
        type: "metrics"
        title: "⚡ Live Metrics"
        data: realtime_data
        refresh_interval: 30
        
        # 📊 Metric cards
        metrics: [
            {
                name: "🔥 Active Users"
                value: realtime_data.active_users
                trend: realtime_data.active_users_trend
                format: "#,##0"
                color: "success"
            }
            {
                name: "⚡ API Calls/sec"
                value: realtime_data.api_calls_per_second
                trend: realtime_data.api_trend
                format: "#,##0"
                color: "primary"
            }
            {
                name: "💾 Server Load"
                value: realtime_data.server_load
                trend: realtime_data.load_trend
                format: "#.#%"
                color: realtime_data.server_load > 0.8 ? "danger" : "success"
            }
            {
                name: "📈 Response Time"
                value: realtime_data.avg_response_time
                trend: realtime_data.response_trend
                format: "#ms"
                color: realtime_data.avg_response_time < 200 ? "success" : "warning"
            }
        ]
        
        # 📊 Mini charts
        sparklines: [
            {
                metric: "active_users"
                data: realtime_data.active_users_history
                color: "success"
            }
            {
                metric: "api_calls_per_second"
                data: realtime_data.api_history
                color: "primary"
            }
        ]
        
        # 🧠 Accessibility
        accessibility: {
            alt_text: "Real-time metrics panel showing active users, API calls, server load, and response time"
            screen_reader_friendly: true
        }
    })
}

# 📋 Summary Statistics Panel
function create_summary_panel(sales_data, user_data) {
    # 📊 Calculate key metrics
    total_revenue ← sales_data.sum("revenue")
    total_users ← length(user_data)
    avg_order_value ← sales_data.average("revenue")
    growth_rate ← calculate_growth_rate(user_data)
    
    # 📊 Create summary panel
    return viz_config.panel({
        type: "summary"
        title: "📋 Key Metrics Summary"
        
        # 📊 KPI cards
        kpis: [
            {
                title: "💰 Total Revenue"
                value: total_revenue
                format: "$#,##0"
                change: "+12.5%"
                change_type: "positive"
                icon: "dollar_sign"
                color: "success"
            }
            {
                title: "👥 Total Users"
                value: total_users
                format: "#,##0"
                change: "+8.3%"
                change_type: "positive"
                icon: "users"
                color: "primary"
            }
            {
                title: "📊 Avg Order Value"
                value: avg_order_value
                format: "$#,##0.00"
                change: "+2.1%"
                change_type: "positive"
                icon: "shopping_cart"
                color: "warning"
            }
            {
                title: "📈 Growth Rate"
                value: growth_rate
                format: "#.#%"
                change: "+1.2%"
                change_type: "positive"
                icon: "trending_up"
                color: "success"
            }
        ]
        
        # 📊 Quick insights
        insights: [
            "🎯 Revenue increased by 15% compared to last month"
            "👥 User engagement is at an all-time high"
            "📦 Product category 'Electronics' showing strongest growth"
            "🌍 North America region leading in performance"
        ]
        
        # 🧠 Accessibility
        accessibility: {
            alt_text: "Summary panel showing key business metrics and insights"
            structured_data: true
        }
    })
}

# 🔧 Helper Functions

function calculate_growth_rate(user_data) {
    # 📊 Calculate month-over-month growth
    current_month ← user_data.filter(
        "signup_date >= date('now', '-1 month')"
    ).length()
    
    previous_month ← user_data.filter(
        "signup_date >= date('now', '-2 months') AND signup_date < date('now', '-1 month')"
    ).length()
    
    if previous_month == 0 {
        return 0
    }
    
    return ((current_month - previous_month) / previous_month * 100).round(1)
}

function format_date(date_field, format) {
    # 📅 Format date helper
    return DateTime.format(date_field, format)
}

# 🚀 Start the visualization
main() {
    print("🎨 Starting Data Visualization Dashboard...")
    print("📍 Dashboard will be available at: http://localhost:8080")
    print("🧠 Features:")
    print("   📊 Interactive charts and visualizations")
    print("   🌍 Geographic mapping")
    print("   ⚡ Real-time metrics")
    print("   🎨 Neurodivergent-friendly design")
    print("   ♿ Full accessibility support")
    
    # 🎨 Create and start dashboard
    dashboard ← create_dashboard()
    dashboard.start()
    
    print("✅ Visualization dashboard is running! 🎉")
    print("💡 Open http://localhost:8080 to explore your data!")
}

# 🧠 Accessibility Features:
# - High contrast color schemes
# - Color-blind safe palettes
# - Large, readable labels
# - Keyboard navigation
# - Screen reader support
# - Alternative text for all visualizations
# - Data table alternatives
# - Minimal animations
# - Clear visual hierarchy
