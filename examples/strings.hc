// examples/strings.hc
// A simple example of string manipulation.

// Define a function that adds an exclamation mark.
// Note: String concatenation uses the '+' operator.
func exclaim(s) {
  return s + "!";
}

block "String Manipulation" {
  let greeting = "Hello, HyperCode";

  // Pipe the string to the exclaim function
  greeting | exclaim -> excited_greeting;

  print(excited_greeting);

  return @success(excited_greeting);
}
