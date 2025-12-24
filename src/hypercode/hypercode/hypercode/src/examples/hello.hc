// examples/hello.hc
/**
 * This is a sample HyperCode program
 * that demonstrates various language features.
 */

// Function to calculate factorial
fun factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Main program
fun main() {
    // Calculate factorial of 5
    var result = factorial(5);
    
    // Print the result with string interpolation
    f"The factorial of 5 is: {result}"
    
    // Demonstrate number literals
    var hex_num = 0xFF;
    var binary_num = 0b1010;
    var large_num = 1_000_000;
    
    // Arrays and loops
    var numbers = [1, 2, 3, 4, 5];
    for (var i = 0; i < numbers.length; i = i + 1) {
        print(numbers[i]);
    }
}

// Run the program
main();