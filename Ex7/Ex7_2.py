from random import randint


def guess_a_number():
    rand_number = randint(0, 9)
    correct_guess = False
    while not correct_guess:
        x = input("Choose a number between 0 to 9:")
        if rand_number == int(x):
            print("You Won!")
            correct_guess = True
        elif int(x) > rand_number:
            print("Your number is greater than the selected number")
        elif int(x) < rand_number:
            print("Your number is smaller than the selected number")


guess_a_number()