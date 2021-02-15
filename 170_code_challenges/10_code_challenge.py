"""
code challenge prompt:

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

if a even and b even
    return less
elif a odd and b even
    return great
elif a even and b odd
    return great
elif a odd and b odd
    return odd
"""

# write your code here
# don't forget to test your code
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b

res = lesser_of_two_evens(6, 10)
print(res)
