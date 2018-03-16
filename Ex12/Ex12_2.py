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
        except ValueError:
            print("Could not convert %s '%s' to type %s. Please try again." % (property, current_input, property_type))
        person[property] = valid_input
print(person)
# ********************************************************************************************************************

# Ex 2


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print('there is no index %d in the list.' % index)


my_list = [0, 1, 2, 3, 4, 5]
print_list_element(my_list, 10)
print_list_element(my_list, 3)
# ********************************************************************************************************************

# Ex 3


def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(l)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


my_dict = {'nums': [1, 2, 3], 'letters': ['a', 'b', 'c'], 'symbols': ['$', '#', '&']}
add_to_list_in_dict(my_dict, 'blabla', 11)
print(my_dict)
add_to_list_in_dict(my_dict, 'nums', 4)
print(my_dict)
