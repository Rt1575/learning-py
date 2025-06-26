add = lambda x, y: x + y
print("Sum:", add(5, 3))


numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)


even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)
