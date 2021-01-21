#Control flow
-   if
-   elif
-   else

```python
if 3 > 2:
    print('its true')
print('outside scope')
```

```python
sleeping_hours = 8
if sleeping_hours > 7:
    print('you can drive')
else:
    print('you cannot drive')
```

```python
num = 4
if num % 2 == 0:
    print('even number')
else:
    print('odd number')
```
```python

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
```

### Ternary Operators in python
-   'true' if True else 'false'
```python
a = 5
if a > 5:
    print('greater than five')
else:
    print("no its not")
# 'true'                   if True else     'false'
print('greater than five') if a > 5 else print("no its not")
```