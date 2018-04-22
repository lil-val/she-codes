from random import randint


def guess_a_number():
    rand_number = randint(0, 9)
    x = input("Choose a number between 0 to 9:")
    if rand_number == x:
        print("You Won!")
    elif int(x) > rand_number:
        print("Your number is greater than the selected number")
    elif int(x) < rand_number:
        print("Your number is smaller than the selected number")


guess_a_number()
