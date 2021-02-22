"""
animal-crackers code challenge

Write a function takes two-word string and returns True if both words
begin with same letter

Example 1:
animal_crackers('Levelheaded Llama')   output: True
explanation:
first word (Levelheaded) starts with letter 'L' and second word in the string (Llama) stars with 'L'
since the two letters are equal, we return true

Example 2:
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

"""
# solution 1
def animal_crackers(text):
    word_list = text.lower().split()
    first = word_list[0]
    second = word_list[1]
    return first[0] == second[0]

res = animal_crackers('Levelheaded Llama')
print(res == True)
res = animal_crackers('Crazy Kangaroo')
print(res == False)
res = animal_crackers('Cute cat')
print((res == True))
"""
# solution 2

def animal_crackers(text):
    word_list = text.lower().split()
    print(word_list)
    return word_list[0][0] == word_list[1][0]


res = animal_crackers('Levelheaded LlamA')
# print(res == True)
# res = animal_crackers('Crazy Kangaroo')
# print(res == False)
# res = animal_crackers('Cute cat')
# print(res == True)
