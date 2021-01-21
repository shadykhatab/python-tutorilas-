### Comparison Operators

[![comparison operators in python [Arabic]](http://img.youtube.com/vi/QLLCT1iYp8E/0.jpg)](http://www.youtube.com/watch?v=QLLCT1iYp8E "comparison operators in python [Arabic]")

| Operator | Description                                                                                                       | Example               |
| -------- | ----------------------------------------------------------------------------------------------------------------- | --------------------- |
| \==      | If the values of two operands are equal, then the condition becomes true.                                         | (a == b) is not true. |
| !=       | If values of two operands are not equal, then condition becomes true.                                             | (a !\= b) is true.    |
| \>       | If the value of left operand is greater than the value of right operand, then condition becomes true.             | (a > b) is not true.  |
| <        | If the value of left operand is less than the value of right operand, then condition becomes true.                | (a < b) is true.      |
| \>=      | If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. | (a >= b) is not true. |
| <=       | If the value of left operand is less than or equal to the value of right operand, then condition becomes true.    | (a <= b) is true.     |

```python
print(2 == 2)
print(2 == 1)
print('hello' == 'bye')
print('hello' == 'Hello')
print(2.0 == 2)
#---------------
print(3 != 3)
print(4 != 5)
print(1 > 2)
print(2 < 5)
#---------------
print(2 >= 2)
print(4 <= 1)
```
-We can use logical operators to combine comarisons:
    - and
    - or
    - not
```python
print(1 < 2 < 3)
print(1 < 2 > 3)

print(1 < 2 and 2 > 3)
print(1 < 2 and 2 < 3)
print(('h' == 'h') and (2 == 2))

print((1 == 1) or (2 == 2))
print((100 == 1) or (200 == 200))


print(not True)
print(not False)

print(not (1 == 1))
print(400 > 500)
print(not(400 > 500))
```