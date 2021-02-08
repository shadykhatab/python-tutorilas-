"""
makes twenty code challenge

Given two integers, return true if the sum of the integers is 20 or if one
of the integers is 20. If not, return false

Example 1:
makes_twenty(20, 10)   output: True
explanation:
one of the two parameters equals 20

Example 1:
makes_twenty(18, 2)   output: True
explanation:
the summation result of the two parameters equals 20

Example 3:
makes_twenty(2, 3)   output: False
explanation:
- non of the parameters equal 20
- the summation result of the two parameters does not equals 20

"""

# write your code here
# don't forget to test your code
def makes_twenty(n1, n2):
    if n1 + n2 == 20:
        return True
    elif n1 == 20:
        return True
    elif n2 == 20:
        return True
    else:
        return False

print(makes_twenty(18, 2) == True)
print(makes_twenty(20, 2) == True)
print(makes_twenty(3, 2) == False)

def makes_twenty(n1, n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20


print(makes_twenty(18, 2) == True)
print(makes_twenty(20, 2) == True)
print(makes_twenty(3, 2) == False)