class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"My name is {self.name} and I am {self.age} years old."

p = Person("Rakshit", 20)
print(p.greet())
