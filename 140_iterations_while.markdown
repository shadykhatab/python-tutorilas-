# Syntax
```dtd
while some_boolean_condition
    #do something
else
   # do something different
```

# infinite loop
```python
i = 1
while i < 6:
    print(i)
```
```python
i = 1
while i < 6:
    print(i)
    i += 1
```
# We can use break, continue, and pass statements in out loops to add additional functionality for various cases.
The three statements are defined by:
    1- break: Breaks out of the current closest enclosing loop.
    2- continue: Goes to the top of the closest enclosing loop.
    3- pass: Does nothing at all.

# The break Statement
```python
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
```

# The continue Statement
```python
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

```
# The else Statement
```python
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

```

```python
x = [1, 2, 3]
for item in x:
    pass
print("end")
```

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in nums:
    if n % 2 == 0 or n % 3 == 0:
        print(n)
```
