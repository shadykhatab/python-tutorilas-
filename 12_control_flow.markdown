#Control flow
-   if
-   elif
-   else

```python
if True:
    print('its true')

if 3 > 2:
    print('its true')

sleeping_hours = 8
if sleeping_hours > 7:
    print('you can drive')
else:
    print('you cannot drive')

num = 4
if num % 2 == 0:
    print('even number')
else:
    print('odd number')
```

```python
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
```