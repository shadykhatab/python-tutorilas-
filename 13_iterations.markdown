### for loop
```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for element in my_list:
    print(element)

for x in my_list:
    print(x)

for num in my_list:
    if num % 2 == 0:
        print(num)

list_sum = 0
for num in my_list:
    list_sum = list_sum + num
print(list_sum)
```

```python
my_name = 'shady'
for letter in my_name:
    print(letter)

for _ in my_name:
    print(_)
```

```python
my_list = [(1, 2), ('m', 's'), (2.5, 6.2)]
for item in my_list:
    print(item)
```

```python
list_sum = 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
for num in my_list:
    list_sum = list_sum + num
print(list_sum)
```

```python
list_of_tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]

print(type(list_of_tuples))
for item in list_of_tuples:
    print(type(item))
    print(item)
print("=== End")

for (item1, item2) in list_of_tuples:
    print(item1)
    print(item2)
    print("----------")
```

```python
my_dictionary = {'day1': "Sunday", 'day2': 'Monday', 'day3': "Tuesday"}

for k in my_dictionary:
    print(k)

for k in my_dictionary:
    print(my_dictionary[k])

for e in my_dictionary.items():
    print(e)
    print(type(e))

for k, v in my_dictionary.items():
    print(k)
    print(v)
    
for v in my_dictionary.values():
    print(v)

for k in my_dictionary.values():
    print(k)
```