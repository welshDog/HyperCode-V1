# Simple Hello World in HyperCode
say "Hello, HyperCode!"

# Basic arithmetic
let x = 10 + 5 * 2
print "10 + 5 * 2 = " + str(x)

# Conditional
if x > 15
    print "x is greater than 15"
else
    print "x is 15 or less"
end

# Function definition
func greet(name)
    return "Hello, " + name + "!"
end

# Function call
let message = greet("User")
print message
