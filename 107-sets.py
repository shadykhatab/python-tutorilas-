"""
Sets
    in math: set is a group of unique elements
    - declare
    - union, intersection, symmetric_difference, difference
    - Examples
    - unique tags
    - users taking two actions
"""


a = {1, 2, 3}
b = {3, 4, 5}
c = {1, 2, 2, 2, 2, 3}
print(c)
print(a | b)

d = {1, 2, 3}
f = {2, 3, 4}

# union
print(d | f)
# print(d + f)
print(a.union(b))

# intersection
print(d & f)
print(a.intersection(b))


print(d - f)
print(d.difference(b))

# symmetric diffrenece everything that is unique
print(d ^ f)
print(d.symmetric_difference(b))

# work the same way with strings
a = set('banana')
b = set('scarab')
print(a | b)


# set out of list
basket = ['apple', 'banana', 'orange','apple', 'banana', 'orange' ]
print(basket)
print(set(basket))