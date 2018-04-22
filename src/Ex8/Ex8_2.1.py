def multiple(a, b):
    # takes in two numbers and recursively multiplies them together
    if a == 1:
        return b
    elif a == 0:
        return 0
    else:
        return b + multiple(a - 1, b)


print(multiple(0, 5))
print(multiple(5, 4))
print(multiple(3, 0))
