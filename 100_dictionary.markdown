# Example:
-   Unordered
-   Changeable / Mutable
-   
```python

person = { 
  "name": "Mohamed Ali", 
  "job": "Boxer"
} 
print(car["brand"]) 
 
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

```python
prices = {
    "orange": {"Sat": 1.4, "Mon": 2.5},
    "banana": {"Sat": 4.5, "Mon": 5.6}
}

print(prices["orange"]["Sat"])


car_models = {
    "ford" : ["fusion", "mustang", "ranger"],
    "toyota": ["corolla", "yaris", "camry"]
}
```

# different ways to declare dictionaries
```python
player = dict(
    first_name="mohamed",
    last_name="ali",
    age=40,
    interests=['reading', 'programming']
)

keys = ['first_name', 'last_name', 'age', 'interests']
values = ["mohamed","ali", 40, ['reading', 'programming'] ]
player = dict(zip(keys, values))
```