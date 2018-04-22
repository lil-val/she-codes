# Ex 1
person = {}
properties = [
    ('name', str),
    ('surname', str),
    ('age', int),
    ('height', float),
    ('weight', float)
]

for property, property_type in properties:
    valid_input = False
    while not valid_input:
        try:
            current_input = input("Please enter your %s: " % property)
            valid_input = property_type(current_input)
        except ValueError as e:
            print(e)
        person[property] = valid_input
print(person)
# ************************************************************************************

# Ex 2


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError as e:
        print('there is no index %d in the list.' % index)
        raise e


my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print_list_element(my_list, 3)
print_list_element(my_list, 10)
