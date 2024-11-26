""" DICTIONARIES
Similar to objects in javascript. Contains a key and a value
"""

favorite_animal = 'dog' # A variable can be used as a key as well

student = {
    'name': 'Maria', # Keys must be in quotes
    'favorite_number': 5, # Values can be anything
    favorite_animal: 'llama' # notice the lack of quotes around favorite_animal
}

print(student)
# prints: {'name': 'Maria', 'favorite_number': 5, 'dog': 'llama'}
# note the 'dog' key - the value of the favorite_animal variable is used

# Use Square bracket notation to access specific items

name = student['name']
print(name)
# prints: Maria

""" ERROR PROTECTION """

# Use the .get() method

# favorite_food = student['favorite_food']
# error: KeyError: 'favorite_food'

print(student.get('favorite_food'))
# prints: None

# Or if/else

if 'course' in student:
    print(f"{student['name']} is enrolled in {student['course']}")
else:
    print(f"{student['name']} is not enrolled in a course")
    # prints: Maria is not enrolled in a course
    
""" Dictionary MUTATION """

# Add item - If it doesn't exist, it gets added 

student['age'] = 25
print(student)

# Modify Item - If it exists, it is modified

student['name'] = 'Mariana'
print(student['name'])
# prints: Mariana


# Delete Item - del to remove it entirely

del student['dog']
# verify that the item was deleted
print('dog' in student)
# prints: False

""" DICTIONARY ITERATION """

for key, val in student.items():
    print(f"{key} is {val}")
    # prints:
    # name is Maria
    # favorite_number is 5
    # age is 25

where_my_things_are = {
    'Headphones': 'On my head',
    'Phone': 'In my left pocket',
    'Wallet': 'In my right pocket',
    'PS5': 'On top of my drawer'
}

for thing, location in where_my_things_are.items():
    print(f'My {thing} is in my {location}')