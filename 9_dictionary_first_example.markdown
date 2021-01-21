Dictionaries 
- Dictionaries are unordered mappings for storing objects. 
- Dictionaries use a Key-Value pairing instead. 
- The Key-Value pair allows you to quickly grab objects without needing to know an index location 
- Example: {“key1”: “value1”, “key2”: “value2”} 
- Differences between dictionary and list: 
- Dictionaries: objects retrieved by key name. Unordered. 
- Lists: objects retrieved by index. Can be sliced and indexed.
```python
""" 
Unordered 
When we say that dictionaries are unordered, it means that the items does not have a defined order, 
you cannot refer to an item by using an index. 
 
Changeable 
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created. 
 
Duplicates Not Allowed 
Dictionaries cannot have two items with the same key: 
 
Dictionary Items - Data Types 
The values in dictionary items can be of any data type: 
 
""" 
thisdict = { 
  "brand": "Ford", 
  "model": "Mustang", 
  "year": 1964 
} 
print(thisdict["brand"]) 
 
thisdict = { 
  "brand": "Ford", 
  "model": "Mustang", 
  "year": 1964, 
  "year": 2020 
} 
print(thisdict) 
 
print(len(thisdict)) 
 
thisdict = { 
  "brand": "Ford", 
  "electric": False, 
  "year": 1964, 
  "colors": ["red", "white", "blue"] 
} 
thisdict["brand"] = "VOLOV CAR 2021" 
print(thisdict) 
print(type(thisdict)) 
print(thisdict["colors"]) 
 
thisdict.pop("brand") 
thisdict.pop("electric") 
thisdict.pop("year") 
thisdict.pop("colors") 
print(thisdict) 
 
prices_lookup = {'apple': 2.99, 'orange': 1.99, 'milk': 5.80} 
print(prices_lookup['apple']) 
orange_price = prices_lookup['orange'] 
print(orange_price) 
 
# dictionary contains another dictionary 
my_dict = { 
    "students": {1: "james", 2: "john"}, 
    "teachers": {1: "teacher1", 2: "teacher2"} 
} 
print(my_dict["students"])  # {1: 'james', 2: 'john'} 
print(my_dict["students"][1]) 
 
 
# dictionry contains list 
alphabet = { 
    "lower": ['a', 'b', 'c'], 
    "upper": ['A', 'B', 'C'] 
} 
print(alphabet) 
print(alphabet["lower"]) 
# alphabet["lower"] returns list, can be sliced and indexed 
print(alphabet["lower"][1]) 
# alphabet["lower"][1] return string, string manipulation can be done 
print(alphabet["lower"][1].upper()) 
prices = { 
    "orange": 10, 
    "banana" : 20 
} 
 
print(prices["orange"] + prices["banana"]) 
car = { 
    "color": ["white", "black"] 
} 
 
x = car["color"][1] 
 
print(x) 
``` 