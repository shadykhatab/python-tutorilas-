## The names you use when creating these labels need to follow a few rules: 
1. Names cannot start with a number. 
2. There can be no spaces in the name, use _ instead. 
3. Can't use any of these symbols (special character):'", <>/? |\()!@#$%^&*~-+ 
4. It's considered best practice (PEP8) that names are lowercase. 
5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),    or 'I' (uppercase letter eye) as single character variable names. 
6. Avoid using words that have special meaning in Python like "list" and "str"
 ---
## Dynamic Typing 
```python
my_dogs = 2 
my_dogs = ['Sammy', 'Frankie'] 
```

#### Pros and Cons of Dynamic Typing 
- Pros:
    -   very easy to work with 
    -   faster development time 
-   Cons:
    -   may result in unexpected bugs! 
    -   you need to be aware of `type()`