// Golden Example for HyperCode
// This file serves as the living specification and testbed for the Golden Syntax.

block "Main Execution" {
  let start_value = 5;

  // Use the pipe to chain operations with the new native functions
  // 1. Start with start_value (5)
  // 2. Pipe it to the native 'double' function (result: 10)
  // 3. Pipe that result to the native 'square' function (result: 100)
  // 4. Assign the final result to the 'final_result' variable
  start_value | double | square -> final_result;

  print(final_result);

  return @success(final_result);
}
