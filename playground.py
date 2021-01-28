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