// Basic OOP in HyperCode
class Animal {
    init(name) {
        this.name = name
    }

    speak() {
        print("...")
    }
}

class Dog extends Animal {
    speak() {
        print("Woof!")
    }
}

let dog = Dog("Buddy")
print(dog.name)  // Output: Buddy
dog.speak()      // Output: Woof!
