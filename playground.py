'''
Lecture 12 (Flow Control) (If Conditions)
if  elif    else
Ternary Operator
'''
#

'''
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
'''

grade = 50

if 90 <= grade <= 100:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
elif 60 <= grade <= 69:
    print("D")
else:
    print("F")