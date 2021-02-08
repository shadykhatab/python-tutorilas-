# *args

```python
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))
```

```python
# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))
```

```python
def my_func(*names):
    for x in names:
        print(x, end=" ")


my_func('hello', 'world')
```

# **kwargs
```python
def my_func(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}.'.format(kwargs['fruit']))
    else:
        print('I did not finc fruits')


my_func(fruit='apple', veggie='lettuce')

```

# *args and **kwargs