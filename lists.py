""" 
LISTS
Literally just JavaScript arrays
You learned python first, you knew lists first. You know this ShirtHanger
"""

colors = ['red', 'green', 'blue']

""" Accessing items """

# Via index...
print(colors[0])
# prints: red

# Or negative index, from right to left, unlike JS
print(colors[-1])
# prints: blue

""" LIST MUTATION """

# Modify item

colors[-1] = 'brown'
print(colors)
# prints: ['red', 'green', 'brown']

# Add One item

colors.append('purple')
print(colors)
# prints: ['red', 'green', 'brown', 'purple']
# purple was added to the END of the list


# Add multiple items
colors.extend(['orange', 'black'])
print(colors)
# prints: ['red', 'green', 'brown', 'purple', 'orange', 'black']
# orange and black were added to the END of the list

# Insert item

colors.insert(1, 'yellow')
print(colors)
# prints: ['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']
# yellow was added at the 1 index; no elements were replaced

# Remove item
# .pop() stores it in a variables
green = colors.pop(2)
print(colors)
print('Removed color', green)
# prints: ['red', 'yellow', 'brown', 'purple', 'orange', 'black']
# prints: green
# green was removed at the 2 index and is in the green variable

# .remove() just deletes it altogether, targetting by name
colors.remove('orange')
print(colors)
# prints: ['red', 'yellow', 'brown', 'purple', 'black']

# .clear() empties a list

colors.clear()
print(colors)
# prints: []

""" LIST ITERATION """

# Just use a for loop lol

colors = ['red', 'green', 'blue']
for color in colors:
    print(color)
    # prints:
    # red
    # green
    # blue

# If you wanna get technical, you can access the index as well with enumerate()

for idx, color in enumerate(colors):
    print(idx, color)
    # prints:
    # 0 red
    # 1 green
    # 2 blue
