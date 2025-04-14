my_dict = {
    'list': ['Portugal', 'Spain', 'Denmark', 'Bahrain', 'Italy'], 'tuple': ('one', 2, True, 'four', 5, 2),
    'dict': {'Apple': 'red', 'Lime': 'yellow', 'Pineapple': 'green', 'Carrot': 'orange', 'Tomato': 'dark red'},
    'set': {1, 3, 5, 5, 9, 'one', 'one', True, False, 32}}

# print last item from "tuple"
print(my_dict['tuple'][-1])

# actions with 'list': add and remove element
my_dict['list'].append('Poland')
my_dict['list'].pop(1)

# actions with 'dict': add and remove
my_dict["dict"][("i am a tuple",)] = "you are not"
my_dict['dict'].pop('Lime')

# action with 'set': add and remove
my_dict['set'].add(18)
my_dict['set'].remove(5)

# print the whole dictionary
print(my_dict)
