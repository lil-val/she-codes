def print_stars(x):
    #print required amount of stars into  "str"
    return "* " * x


def print_triangle(y):
    for x in range(1, y):
        print(" " * (y-x) + print_stars(x))


def print_trapeze(a,b):
    for x in range(a, b):
        print(print_stars(x))


def print_rhombus(y):
    for x in (list(range(1, y)) + list(range(y, 0, -1))):
        print(" " * (y - x) + print_stars(x))


(print_triangle(5))
print(" ")
(print_trapeze(3, 7))
print(" ")
print_rhombus(5)
