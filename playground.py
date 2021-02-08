"""
Write a function that returns the lesser of two given numbers if both numbers are even,
but returns the greater if one or both numbers are odd.

Ex:
lesser_of_two_evens(2, 4)   --> 2
lesser_of_two_evens(2, 5)   --> 5
"""


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


res1 = lesser_of_two_evens(2, 4)
print(res1 == 2)
res2 = lesser_of_two_evens(2, 5)
print(res2 == 5)
res3 = lesser_of_two_evens(7, 5)
print(res3 == 7)

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

