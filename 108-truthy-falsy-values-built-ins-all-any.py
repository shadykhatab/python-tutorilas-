is_active = True
is_admin = False

20 > 10
True
20 < 10
False

'a' < 'b'
'a' > 'b'

bool('Hi')
bool('')
bool(100)
bool(0)



# false values in python
# The number zero (0)
# An empty string ''
# False
# None
# An empty list []
# An empty tuple ()
# An empty dictionary {}

# any: is there any truthy value
# all: are all the values truthy
list = [True, True, True]
print(any(list))
print(all(list))

nums = [0, 0, 0]
print(any(nums))
print(all(nums))

print(any([[], ( ), {}, None, 0]))
print(any([[0], ( ), {}, None, 0]))


nums = [10, 20, 30]

for x in nums:
    print(x)

res = any([x > 10 for x in nums])
print(res)

nums = [0, 0, 9]