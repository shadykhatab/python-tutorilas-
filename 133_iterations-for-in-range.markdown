### Python range function
### for-in-range

    - range() is a built-in function of Python. It is used when a user needs to perform an action for a specific number of times
    - The range() function is used to generate a sequence of numbers.
```python
for i in range(10): 
    print(i, end =" ") 
print()
```

### Syntax
range(stop) takes one argument.
range(start, stop) takes two arguments.
range(start, stop, step) takes three arguments.

```python
for i in range(1, 20): 
    print(i, end =" ") 
print() 
  
# printing a natural 
# number from 5 t0 20 
for i in range(5, 20): 
    print(i, end =" ") 
```

```python
for i in range(0, 30, 3): 
    print(i, end = " ") 
print() 
  
# using range to print number 
# divisible by 5 
for  i in range(0, 50, 5): 
     print(i, end = " ") 
```

### Increment & Decrement
```python
# incremented by 3 
for i in range(15, 25, 3): 
    print(i, end =" ") 

# incremented by -3 
for i in range(25, -6, -3): 
    print(i, end =" ") 
```