##Primitive Types in Python
Python has 4 primitive data types:
1)	Integers (ex. 1, 2, 3)
2)	Float (ex. 1.2, 2.5, 5.8)
3)	Strings (ex. "Alexandria", "John", "Tony")
4)	Boolean (True, False)

## What is a list?  
A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.    
They use [] brackets and commas to separate objects in the list.  

Examples:
```python
list_of_integers = [1, 2, 3, 4]   
list_of_strings = ["CA", "NY", "AL", "AK"]    
random_list = [1, 2 , "Hennery", "AR", 34.56]
``` 

---
 ## Examples:
```python
list_of_integers = [1, 2, 3, 4]   
list_of_strings = ["CA", "NY", "AL", "AK"]    
random_list = [1, 2 , "Hennery", "AR", 34.56]
``` 

## Access Elements in Python List (Indexing Lists)

- Each item in a list corresponds to an index number, which is an integer value, starting with the index number 0.
- we can also access items from the list with a negative index number, by counting backwards from the end of the list, starting at -1. 

```python
colors = ["Blue", "White", "Red"]
first_color = colors[0]
print(first_color)

white_color = colors[1]
print(white_color)
print(colors[-1])
```
|    |            |   | |
|----------|:-------------:|------:|------:|
| Negative Element Index |  -3 | -2 |-1|
| Positive Element Index |    0   |   1 | 2|
| List Elements | "Red" |    "Blue" | "White"|

# IndexError
If we call the list colors with an index number of any that is greater than 2, it will be out of range as it will not be valid:
```python
colors = ["blue", "white", "red"]
print(colors[5])
# output: IndexError: list index out of range
```

# Modifying Items in Lists
```python
nums = [1, 2, 3, 4]
print(nums)
nums[3] = "John"
print(nums)

nums[-4] = 12.75
print(nums)
```
---
#Deleting Items from List

#### 1- Delete Element from python list using del keyword
```python
nums = [1, 2, 3, 4]

del nums[1]
print(nums)
```
#### 2- Delete last element from python list using pop() function
```python
nums = [1, 2, 3, 4]

delete_element = nums.pop()

print(delete_element)
print(nums)
```
###  3- Delete elements by passing index to pop() function
```python
nums = [1, 2, 3, 4]

delete_element = nums.pop(1)

print(delete_element)
print(nums)
```
####  4- Deleting all list elements using clear() function
```python
nums = [1, 2, 3, 4]

nums.clear()
print(nums)
```
####  5- Delete element from python list using by passing value to remove() function
```python
names_list = ["John", "Tony", "Mark"]

names_list.remove("John")
print(names_list)
```
####  6- Deleting range using del and slicing
```python
nums = [1, 2, 3, 4, 5]
del nums[0:3]
print(nums)
```
---
# Adding Items to python List

#### 1- Using append() function

```python
my_list = ["Olivia", "Emma", "Sophia"]
my_list.append("Mia")
print(my_list)
```
#### 2- Using insert() function
```python
my_list = ["Olivia", "Emma", "Sophia"]
my_list.insert(0, "beginning")
my_list.insert(4, "end")
print(my_list)
```
---
# Modifying Lists with Operators
```python
nums = [1, 2, 3]
days = ["Sat", "Sun", "Mon"]

c = nums + days
print(c)

a = nums + [4, 5, 6]
print(a)

print(nums * 2)
```
---
# Basic List Operations
```python
my_list = [1, 1, 1, 2, 3, 4]
my_len = len(my_list)
print(my_len)

my_count = my_list.count(1)
print(my_count)

i = my_list.index(2)
print(i)

my_list.reverse()
print(my_list)

unsorted_list = [4, 6, 5, 2, 3, 1]
unsorted_list.sort()
print(unsorted_list)
```





