# What is method/function?
    - In Python, a method is a function that is available for a given object because of the object's type.
## Example:
```python
# All lists have an append method simply because they are lists.
my_list=[1, 2, 3]
my_list.append(4)

my_string = 'some lowercase text'
my_string.upper()

```

Lists don't have an upper method, and strings don't have an append method. Why? Because methods only exist for a particular object if they have been explicitly defined for that type of object, and Python's developers have (so far) decided that those particular methods are not needed for those particular objects.

To call a method, the format is object_name.method_name(), and any arguments to the method are listed within the parentheses. The method implicitly acts on the object being named, and thus some methods don't have any stated arguments since the object itself is the only necessary argument. For example, my_string.upper() doesn't have any listed arguments because the only required argument is the object itself, my_string.

- [Python built in functions list](https://docs.python.org/3/library/functions.html)
- [Official Python tutorial and documentation](https://docs.python.org/3/tutorial/index.html)

# Why we need functions?
-   creating clean repeatable code is a key part of becoming an effective programmer.
-   Functions allow us to create blocks of code that can be easily executed many times,
without needing to constantly rewrite the entire block of code.

# Syntax
```dtd
def name_of_function():
    """
      explain the function
    """
    print("hello")
    print("world")

>>> name_of_function()
> output: Hello
> output: world
```

# Syntax
```dtd
def name_of_function(x):
    """
      explain the function
    """
    print("hello " + x)

>>> name_of_function("john")
> output: Hello John
```

- Typically we use the return keyword to send back the result of the function, instead of just printing it out.
- return allows us to assign the output of the function to a new variable

```python
def add_function(num1, num2):
    return num1 + num2

result = add_function(1, 2)
print(result)
```

# Arguments default value
```python
def greet(name="salem"):
    print("hello " + name)

greet()
greet("john")
``` 

```python
def dog_check(my_string):
    if 'dog' in my_string:
        return True
    else:
        return False

result = dog_check("my cat ran away")
print(result)

result = dog_check("my dog barks at everything")
print(result)

result = dog_check("my DOG barks at everything")
print(result)


```