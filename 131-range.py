"""
for-in-range
- range() is a built-in function of Python.
It is used when a user needs to perform an action for a specific number of times
- The range() function is used to generate a sequence of numbers.
"""

nums = range(10)
list(nums)

counters = range(1, 11)
list(counters)

fives = range(0, 50, 5)
list(fives)

fives = range(0, 51, 5)
list(fives)

test = range (51, 5)
list(test)

items = ['a', 'b', 'c']

for i in range(len(items)):
    print(items[i])