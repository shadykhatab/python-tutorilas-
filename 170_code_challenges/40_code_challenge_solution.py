"""
write a function that capitalizes the first and fourth letters of a name
ex:
capitalize("macdonald") --> MacDonald
"""


# solution 1
def capitalize(name):
    first_letter = name[0]
    in_between = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
    return first_letter + in_between + fourth_letter + rest


result = capitalize("macdonald")
print(result)

result = capitalize("macarthur")
print(result)


# solution 2
def capitalize(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()


result = capitalize("macdonald")
print(result)

result = capitalize("macarthur")
print(result)
