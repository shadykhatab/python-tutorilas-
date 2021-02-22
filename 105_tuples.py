"""
Tuples (Immutability)
declare,
special declaration: empty tuple & single item tuple

cannot append, remove or sort in place
intro to sorted function

tuple can contain different data types and structures

example of list contains tuples

min max sum len

"""

# declare
a = (1, 2, 3, 4, 5)
b = ('a', 'b', 'c', 'd')
c = 10, 20, 30
empty = ()
single = (1,)
single = ("a",)

print(a)
print(b)
print(c)


# cannot append, remove or sort in place

# a.append(99)
# a.remove()
# a.sort()

# intro to sorted function

shopping = ('apples', 'milk', 'bread')
alppaShopping = sorted(shopping)
alppaShopping = tuple(sorted(shopping))
print(alppaShopping)


# tuple can contain different data types and structures
shopping_stops = (
    ['bread', 'milk', 'eggs'],
    ['picture hooks', 'extension cord']
)

print(shopping_stops)
print(shopping_stops[0])
shopping_stops[0].append('apples')
print(shopping_stops)


# example of list contains tuples
users = [(1, 'user_a'), (1, 'user_b')]
print(users)

scores = (15, 66, 34, 99, 29, 54, 12)
# min max sum len
print(max(scores))
print(min(scores))
print(sum(scores) / len(scores))

print(sorted(scores))
print(tuple(sorted(scores)))


# returning tuple from function

def min_max(nums):
    return min(nums), max(nums)


my_nums = (1, 2, 4, 5, 7, 4, 3)
result = min_max(my_nums)
print(result)
(lowest, highest) = result
print(lowest)