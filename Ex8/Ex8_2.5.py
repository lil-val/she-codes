def reverse_string(text):
    #takes in a string and returns a reversed copy of the string.
    #The only string operation you are allowed to use is string concatenation.
    if len(text) <= 1:
        return text
    else:
        return text[-1] + reverse_string(text[:-1])


print(reverse_string("A"))
print(reverse_string(""))
print(reverse_string("bla bla"))
print(reverse_string("Lilach!"))
