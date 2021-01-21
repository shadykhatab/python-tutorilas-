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