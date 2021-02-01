"""
Control flow if, elif, else
a: "90 - 100"
b: 80 - 90
c : 70 - 80
"""
grade = 50

if 90 <= grade <= 100:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
else:
    print("F")