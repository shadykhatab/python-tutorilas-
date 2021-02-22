# String 
- Strings are sequences of characters, using the syntax of either single quotes or double quotes. 
- White space counts as a character. 
```python
a = 'hello' 
b = "hi" 
c = " He’s is ”so” fine " 
```

### Escape Sequence 
  
```python
a = "we're \" so \" fine" 
 
print(a) 
 
print('hello \n world')
print('hello \t world') 
len('hello')
 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

""" 
escape sequences 
1- \" ( double quote ) 
    ex: a = "we're  \"so\" fine" 
2- \n ( new line ) 
    ex: a = "we're \n fine" 
3- \t ( tab = 2 spaces ) 
    ex: a = "we're\t fine" 
""" 
 
a = "we're\t fine" 
 
print(a) 
```
 
 ---
 
- Strings can be indexed and sliced. 
- Indexing uses [] notation after the string. 
- Indexing allows you to grab a single character from the string.

| H  | E  | L  | L  | O  |
|----|----|----|----|----|
| 0  | 1  | 2  | 3  | 4  |  

| H  | E   | L   | L   | O   |
|----|-----|-----|-----|-----|
| -5  | -4  | -3  | -2  | -1  |

```python
greeting = 'hello' 
a = len(greeting) 
print(a) 
print(greeting[0]) 
print(greeting[1]) 
print(greeting[-1]) 
```
### Slice allows you to grab a subsection of multiple characters, a “slice” of the string”.
-   This has the following syntax: 
-   String[start : stop : step] 
-   Start: is a numerical index for the slice start 
-   Stop is the index you will go up to (but not include) 
-   Step is the size of the “jump” you take. 
```python
# create a variable 
alphabet = 'abcdefghijklmnopqrstuvwxyz' 
 
# string slice from index 2 to the end of the string 
var1 = alphabet[2:] 
print(var1) 
 
# string slice from 0 the the end 
var2 = alphabet[:] 
print(var2) 
 
# string slice from 0 to index 3 
var3 = alphabet[:3] 
print(var3) 
 
# slice from index 2 to index 5 
var4 = alphabet[2:5] 
print(var4) 
 
# slice from 0 to end and skip 2 
var5 = alphabet[::2] 
print(var5)
```
-   Slicing with negative steps 
```python
alphabet = '12345' 
 
var5 = alphabet[::-1] 
print(var5)
```

-   important String methods
```python
# String concatenation 
x = "hello" 
y = "world" 
print(x + " " + y) 
 
x = '2' 
y = '3' 
print(x + y) 
 
# String multiplication 
x = "word" 
print(x * 10) 
 
# some string methods/functions 
name = "shady" 
print(name.upper()) # converts all chars to uppercase 
print(name) # upper() doesn't change the original string 
name = name.upper() # now we have changed to original string 
print(name) 
name = "EGYPT" 
print(name.lower()) # converts all chars to lowercase 
 
name = "Shady Mostafa Abdelmageed Abdelhalim Khatab" 
print(name.split())  # split function by default will split a sentence on spaces 
sentence = "I'mzlearningzprogramming" 
print(sentence.split('z')) 
```
---
### String format
```python
x = "I'm {}".format("happy") 
print(x) 
 
x = "I'm {}".format("happy", "well") 
print(x) 
 
x = "I'm feeling {} {}".format("ver", "well") 
print(x) 
 
x = "I'm feeling {1} {0}".format("well", "very") 
print(x) 
 
x = "I'm feeling {0} {0} {0}".format("good", "happy", "excited") 
print(x) 
 
x = "My name is {name}".format(age=4, name= "salem", location="san jose") 
print(x) 
x = "I live in {location}".format(age=4, name= "salem", location="san jose") 
print(x) 
 
x = 100 / 777 
print("the result was {}".format(x)) 
print("the result was {r}".format(r=x)) 
print("the result was {r:1.3f}".format(r=x)) 
print("the result was {r:1.4f}".format(r=x)) 
print("the result was {r:1.5f}".format(r=x)) 
print("the result was {r:10.5f}".format(r=x)) 
 
 
name = 'jose' 
print("my name is {}".format(name)) 
print(f"my name is {name}") 
 
name = 'salem' 
age = 4 
location = 'san jose' 
print(f"his name is {name}, he's {age}, and he lives in {location}") 
```