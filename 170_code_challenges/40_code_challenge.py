"""
write a function that capitalizes the first and fourth letters of a name
ex:
capitalize("macdonald") --> MacDonald

declare function
get first letter
get in between letter
get fourth letter
get rest of letters
return concatenated string
"""
def capitalize (name):
    first_letter = name[0]
    between_letter = name[1:3]
    fourth_letter = name[3]
    rest_letter = name[4:]
    return first_letter. upper()+ between_letter+fourth_letter.upper()+rest_letter
print(capitalize('macdonald'))












