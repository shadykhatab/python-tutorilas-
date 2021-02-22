"""
animal-crackers code challenge

Write a function takes two-word string and returns True if both words
begin with same letter

Example 1:
animal_crackers('Levelheaded Llama')   output: True
explanation:
first word (Levelheaded) starts with letter 'L' and second word in the string (Llama) stars with 'L'
since the two letters are equal, we return true

Example 1:
animal_crackers('Crazy Kangaroo')   output: False
explanation:
first word (Crazy) starts with letter 'C' and second word in the string (Kangaroo) stars with 'K'
since the two letters C and K aren't equal, we return false

Example 3:
animal_crackers('Cute cat')   output: True
explanation:
first word (Cute) starts with letter 'C' and second word in the string (cat) stars with 'c'
since the two letters are equal, we return true

"""

# write your code here
# don't forget to test your code
"""
def animal_crackers(text):
    list= text.split()
    first = list[0]
    second = list[1]
    print(first)
    print(second)
    letterone= list[0][0]
    lettertwo= list[1][0]
    print(letterone)
    print(lettertwo)


    return letterone==lettertwo
    animal_crackers('Levelheaded abc')
"""

def animal_crackers(text):
    list= text.split()
    first= list[0]
    second= list[1]
    print(first)
    print(second)
    letterone= list[0][0]
    lettertwo= list[1][0]
    print(letterone)
    print(lettertwo)
    return letterone == lettertwo
animal_crackers('Levelheaded abc')





