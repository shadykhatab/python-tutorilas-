"""

"""


# def is_same(num1, num2):
#     return num1 == num2
#
#
# print(is_same(4, 8))
# print(is_same(2, 2))
# print(is_same(2, "2"))


# def min2sec(minutes):
#     return minutes * 60
#
# print(min2sec(5))
# print(min2sec(3))
# print(min2sec(2))


# def how_many_legs(chickens, cows, elephants):
#     return chickens * 2 + cows * 4 + elephants * 4
#
#
# print(how_many_legs(2, 3, 5))
# print(how_many_legs(1, 2, 3))
# print(how_many_legs(5, 2, 8))


# def increment(n):
#     return n + 1
#
# print(increment(0))
# print(increment(9))
# print(increment(-3))



# def remainder(m, n):
#     return m % n
#
# print(remainder(1, 3))
# print(remainder(3, 4))
# print(remainder(5, 5))
# print(remainder(7, 2))


# def string_int(s):
#     return  int(s) + 1
#
# print(string_int("199"))

# def clac_exp(m, n):
#     return m**n
#
# print(clac_exp(5, 5))


"""
true    false   false
false   true    false
false   false   false
true    true    true
"""

# def and_test(a, b):
#     return a and b
#
# print(and_test(True, False))
# print(and_test(False, True))
# print(and_test(False, False))
# print(and_test(True, True))

# list = [5, 8, 4, 6, 7]
# print(list)
# list.sort()
# print(list)


# goal
# goooooal
# gooooooooooal

# def long_goal(n):
#     print("g" + ("o" * n) + "al")
#
#
# long_goal(3)
# long_goal(5)
# long_goal(9)


# "MohamedAli" => "Mohamed Ali"
# "HelloWorld" => "Hello World"

# def capital_space(s):
#     result = ""
#     i = 0
#     while i < len(s):
#         if s[i].isupper():
#             result += " "
#         result += s[i]
#         i += 1
#     print(result)
#
# capital_space("HelloWorld")



# c = "apple".count('a')
# print(c)

# def char_count(letter, word):
#     count = 0
#     for char in word:
#         if char == letter:
#             count+=1
#     return count
#
# print(char_count("p", "apple"))



"""
4! = 4 × 3 × 2 × 1 = 24
7! = 7 × 6 × 5 × 4 × 3 × 2 × 1 = 5040
1! = 1
"""

# def factorial(n):
#     total = 1
#     for i in range(1, n+1):
#         total *= i
#     return total
#
# print(factorial(4))
# print(factorial(7))



# def divisable_by_five(n):
#     return n % 5 == 0
#
# print(divisable_by_five(5))
# print(divisable_by_five(-55))
# print(divisable_by_five(37))



# def is_last_character_n(word):
#     return word[-1] == "n"
#
#
# print(is_last_character_n("Dean"))
# print(is_last_character_n("Tom"))
# print(is_last_character_n("Aiden"))

# def compare_length(str1, str2):
#     return len(str1) == len(str2)
#
# print(compare_length("AB", "CD"))
# print(compare_length("ABC", "CD"))


"""
Hex Code
len = 6
starts with #
A-F
#CD5C5c
HEX CODE COLORS
"""

# def is_valid_hex_code(code):
#     if code[0] != "#" or len(code) != 7:
#         return False
#     i = 1
#     while i < len(code):
#         c = code[i].lower()
#         if not c.isdigit():
#             if c != 'a' and c != 'b' and c != 'c' and  c != 'd' and c != 'e' and c != 'f':
#                 return False
#         i += 1
#     return True
#
# print(is_valid_hex_code("#CD5C5c"))
# print(is_valid_hex_code("#eaecee"))
# print(is_valid_hex_code("#eaecf&"))

# GUEST_LIST = {
#   "Kurt": "Germany",
#   "Julia": "France",
#   "Ito": "Japan",
#   "Katherine": "England",
#   "Sam": "Argentina"
# }
#
# def greeting(name):
#     if name not in GUEST_LIST:
#         return "Hi! I'm a guest."
#     return f"Hi! I'm {name} from {GUEST_LIST[name]}."
#
# print(greeting("Kurt"))   #> "Hi! I'm Kurt from Germany."
# print(greeting("Sam"))    #> "Hi! I'm Sam from Argentina."
# print(greeting("Monty"))  #> "Hi! I'm a guest."



# def has_key(dic, key):
#     return key in dic
#
# print(has_key({ "a": 44, "b": 45, "c": 46 }, "a"))


# 34, 15, 88, 2

# def find_smallest(lst):
#     smallest = lst[0]
#     for i in range(1, len(lst)):
#         value = lst[i]
#         print(f"samllest so far: {smallest}")
#         print(f"value: {value}")
#         if value < smallest:
#             print(f"value {value} is smaller than smallest {smallest}")
#             smallest = value
#     return smallest
#
# print(find_smallest([34, 15, 88, 2]))

# def is_empty(dict):
#     return not dict
#
# print(is_empty({}))
# print(is_empty({'a':1}))


# 10, 15, 20, 2, 10, 6
# max_diff

#
# def difference(lst):
#     max = lst[0]
#     min = lst[0]
#     for i in range(1, len(lst)):
#         val = lst[i]
#         if val < min:
#             min = val
#         if val > max:
#             max = val
#     return max - min
#
# print(difference([10, 15, 20, 2, 10, 6]))

# def first_last(lst):
#     return [lst[0], lst[-1]]
#
# print(first_last([5, 10, True]))


# def find_digit_amount(n):
#     length = len(str(n))
#     if(n < 0):
#         return length - 1
#     return length
#
# print(find_digit_amount(-1))


list = [10, 15, 20, 2, 10, 6]
print(sum(list))


