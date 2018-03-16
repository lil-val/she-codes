def seven_boom():
    for i in range(1, 51):
        if i % 7 == 0:
            print("boom")
        else:
            print(i)


def check_user_input(user_input):
    if user_input == "boom":
        return True
    else:
        return user_input.isdigit()


def check_boom(user_input):
    if user_input != "boom":
        print("You lose!")
    return


def seven_boom_with_user():
    user_turn = True
    for i in range(1, 21):
        if user_turn:
            x = input("Enter next number or boom:")
            if not check_user_input(x):
                print("Invalid Input")
                return
            if i % 7 == 0:
                check_boom(x)
            elif i % 7 != 0:
                if x == "boom":
                    print("You lose!")
                    return
            elif int(x) == i:
                pass
            elif int(x) != i:
                print("You lose!")
                return
        else:
            if i % 7 == 0:
                print("Computer says: Boom")
            else:
                print("Computer says: {}". format(i))
        user_turn = not user_turn
    print("You Win!!!")


#seven_boom()
seven_boom_with_user()

