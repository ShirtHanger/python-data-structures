""" 
TUPLES
Like a list, but cannot be mutated or changed. At all.
Defined with parenthesis () instead of brackets []
"""

hello_tuple = ('Hello') # this will not create a tuple
print(type(hello_tuple)) # prints: <class 'str'>

hello_tuple = ('Hello',) # This will, a single item tuple
hello_tuple = 'Hello', #This also works
print(type(hello_tuple))
# prints: <class 'tuple'>

""" 
Because they are immutable, tuples can even be used as keys for dictionaries
"""

""" ACCESSING ITEMS 
Generally the same as lists"""

colors = ('red', 'green', 'blue')
print(colors[1])
# prints: green

# Access index of a tuple item

colors = ('red', 'green', 'blue')
blue_idx = colors.index('blue')
print(blue_idx)
# prints: 2

""" TUPLE ITERATION
Literally the same as lists"""

for color in colors:
    print(color)
    # prints:
    # red
    # green
    # blue

for idx, color in enumerate(colors):
    print(idx, color)
    # prints:
    # 0 red
    # 1 green
    # 2 blue


""" Unpacking tuples

What's this? Something unique? Say it ain't so!

We can unpack a tuple into variables by declaring them like so:
"""

colors = ('red', 'green', 'blue')
red_color, green_color, blue_color = colors
print(red_color, green_color, blue_color)
# prints: red green blue