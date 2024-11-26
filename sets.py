""" SETS

Unordered list of UNIQUE items called 'Elements'

* sets do not allow duplicate elements. 
* Sets are not indexed. 
* Elements in a set can be added and removed but cannot be changed.

Sets are commonly used for mathematical operations like union, intersection, and difference. 
This makes them useful for tasks such as removing duplicates and finding common elements in multiple collections
"""

integer_set = {1, 2, 3, 4, 5} # Create sets with curly braces {}

# Or use .set()

another_int_set = set([5, 6, 7, 8, 9])

chips = ['potato', 'computer', 'fish and']

chips_set = set(chips)

""" SET MANIPULATION """

# Adding elements to a set
chips_set.add('paint')
print(chips_set)
# prints: {'paint', 'fish and', 'potato', 'computer'}
# remember, sets are not ordered - your elements may print in a different order

# Removing elements from a set
chips_set.remove('fish and')
print(chips_set)
# prints: {'potato', 'paint', 'computer'}
# remember, sets are not ordered - your elements may print in a different order

# Note that you cannot modify an item in a set.

""" 
Mathematical operations
Sets can help performing more complex mathematical operations, 
such as discovering overlap between two collections of data - 
check out this tutorial from Real Python for more.
https://realpython.com/python-sets/
"""