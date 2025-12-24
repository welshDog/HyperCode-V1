// Demo 3: Simple Todo - Variables and Logic
// This demonstrates variables, conditionals, and basic data handling

var taskCount = 0;
var completedCount = 0;

// Add tasks
taskCount = taskCount + 1;
print("✅ Added task 1: Write HyperCode");

taskCount = taskCount + 1;
print("✅ Added task 2: Test the compiler");

taskCount = taskCount + 1;
print("✅ Added task 3: Share with community");

// Complete a task
completedCount = completedCount + 1;
print("🎯 Completed a task!");

// Check progress
print("");
print("📊 Todo Summary:");
print("Total tasks:", taskCount);
print("Completed:", completedCount);
print("Remaining:", taskCount - completedCount);

if completedCount == taskCount {
    print("🎉 All done! You're amazing!");
} else {
    print("💪 Keep going! You got this!");
}