import datetime  # we will use this for date objects


class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age

person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())

#Person is the class name, global variable
#person is an instance of the Peron class, global variable
#surname is a parameter passed into the __init__ method, local variablein the scope of the init method
#self is a parameter passed into each instance method of the class, local variable inside the scope of each of the methods
#age(the function name) is a method of the Person class, local variable
#age(the variable inside the function) a local variable inside the scope of the age method
#self.email an example of how we can refer to attributes and methods of an object using a variable which refers to the object, the . operator and the name of the attribute or method
#person.email  is another example of the same thing. In the global scope, our person instance is referred to by the variable name person.
