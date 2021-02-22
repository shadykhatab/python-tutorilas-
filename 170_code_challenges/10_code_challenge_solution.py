"""
Write a function that returns the lesser of two given numbers if both numbers are even,
but returns the greater if one or both numbers are odd.

Example 1:
lesser_of_two_evens(2, 4)   output: 2
explanation:
the two parameters 2 and 4 are even numbers, therefore, we'll return the smallest even number

Example 2:
lesser_of_two_evens(2, 5)   output: 5
explanation:
the first parameter 2 is even, but the second parameter 5 is odd, therefore, we'll return the greatest number

Example 3:
lesser_of_two_evens(7, 5)   output: 7
explanation:
the two parameters are odd, therefore, we'll return the greatest number
"""

# first solution
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result


# testing solution 1
res1 = lesser_of_two_evens(2, 4)
print(res1 == 2)
res2 = lesser_of_two_evens(2, 5)
print(res2 == 5)
res3 = lesser_of_two_evens(7, 5)
print(res3 == 7)

# solution 2
# we can use built in functions from python min and max
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


res1 = lesser_of_two_evens(2, 4)
print(res1 == 2)
res2 = lesser_of_two_evens(2, 5)
print(res2 == 5)
res3 = lesser_of_two_evens(7, 5)
print(res3 == 7)

