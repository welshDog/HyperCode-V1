// data_analysis.hc - Data analysis example in HyperCode

// Sample sales data
const salesData = [
    { id: 1, product: 'Laptop', category: 'Electronics', price: 999.99, units: 5 },
    { id: 2, product: 'Smartphone', category: 'Electronics', price: 699.99, units: 12 },
    { id: 3, product: 'Desk Chair', category: 'Furniture', price: 199.99, units: 8 },
    { id: 4, product: 'Coffee Maker', category: 'Appliances', price: 49.99, units: 15 },
    { id: 5, product: 'Headphones', category: 'Electronics', price: 149.99, units: 20 },
    { id: 6, product: 'Notebook', category: 'Stationery', price: 4.99, units: 50 },
    { id: 7, product: 'Monitor', category: 'Electronics', price: 249.99, units: 7 },
    { id: 8, product: 'Desk Lamp', category: 'Furniture', price: 34.99, units: 18 },
    { id: 9, product: 'Mouse', category: 'Electronics', price: 24.99, units: 25 },
    { id: 10, product: 'Keyboard', category: 'Electronics', price: 79.99, units: 15 }
]

// 1. Calculate total revenue by category
function calculateRevenueByCategory(data) {
    return data.reduce((acc, item) => {
        const total = item.price * item.units
        acc[item.category] = (acc[item.category] || 0) + total
        return acc
    }, {})
}

// 2. Find top selling products
function getTopSellingProducts(data, limit = 3) {
    return [...data]
        .sort((a, b) => (b.price * b.units) - (a.price * a.units))
        .slice(0, limit)
}

// 3. Calculate inventory value by category
function getInventoryValue(data) {
    return data.reduce((acc, item) => {
        const value = item.price * item.units
        if (!acc[item.category]) {
            acc[item.category] = 0
        }
        acc[item.category] += value
        return acc
    }, {})
}

// 4. Format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount)
}

// Main function to run the analysis
function main() {
    console.log('📊 Sales Data Analysis\n')
    
    // 1. Total revenue by category
    const revenueByCategory = calculateRevenueByCategory(salesData)
    console.log('💰 Revenue by Category:')
    for (const [category, revenue] of Object.entries(revenueByCategory)) {
        console.log(`  ${category}: ${formatCurrency(revenue)}`)
    }
    
    // 2. Top selling products
    console.log('\n🏆 Top Selling Products (by revenue):')
    const topSellers = getTopSellingProducts(salesData, 3)
    topSellers.forEach((item, index) => {
        console.log(`  ${index + 1}. ${item.product}: ${formatCurrency(item.price * item.units)} (${item.units} units)`)
    })
    
    // 3. Inventory value
    console.log('\n📦 Inventory Value by Category:')
    const inventoryValue = getInventoryValue(salesData)
    for (const [category, value] of Object.entries(inventoryValue)) {
        console.log(`  ${category}: ${formatCurrency(value)}`)
    }
    
    // 4. Total revenue
    const totalRevenue = Object.values(revenueByCategory).reduce((sum, val) => sum + val, 0)
    console.log(`\n💵 Total Revenue: ${formatCurrency(totalRevenue)}`)
    
    // 5. Categories summary
    const categories = [...new Set(salesData.map(item => item.category))]
    console.log(`\n📈 Total Categories: ${categories.length}`)
    console.log(`📦 Total Products: ${salesData.length}`)
}

// Run the analysis
main()
