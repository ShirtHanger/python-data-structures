""" 
List comprehensions are a powerful feature in Python.

They provide a concise way to create and work with lists. 
They’ll likely seem confusing at first, but they are a favorite of Python fans, 
and you will probably come across them when googling.
"""

""" NUMERICAL EXAMPLE - Mapping

Say we needed to square all of the numbers in a list and put them into a new list, we might use a for loop like this:
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []

# we want 'n * n' for each 'n' in nums 
for n in nums:
    squares.append(n * n)

print(squares)
# prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# List comprehensions can reduce this code
squares = []
for n in nums:
    squares.append(n * n)
# To this, a modified for in loop
squares = [n * n for n in nums]
# List comprehensions always return a new list, leaving the original list unmodified

""" FILTERING
Say we want to filter numbers instead"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = []

# we want 'n * n' for each 'n' in nums  if 'n * n' is even
for n in nums:
    square = n * n 
    if square % 2 == 0:
        even_squares.append(square)

print(even_squares)
# prints: [4, 16, 36, 64, 100]

# List comprehensions can reduce this code
even_squares = []
for n in nums:
    square = n * n 
    if square % 2 == 0:
        even_squares.append(square)
# To this one-liner
even_squares = [n * n for n in nums if (n * n) % 2 == 0]