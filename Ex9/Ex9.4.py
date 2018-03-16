import random, string, re
def cows_and_bulls(actual_str, guess_str):
    bools = 0
    hits = 0
    for char in guess_str:
        for c in actual_str:
            if char == c:
                if guess_str.index(char) == actual_str.index(c):
                    bools += 1
                else:
                    hits += 1
    print('bools: {}, hits: {}'.format(bools, hits))
    return bools


def game(length=5):
    letters = string.ascii_lowercase
    actual_str = ''.join(random.choice(letters) for i in range(length))
    print(actual_str)
    matcher = re.compile('[a-z]{5}')
    x = 0
    while x < 5:
        guess_str = input('please insert a 5 length string: ')
        # if len(guess_str) != 5:
        #     print('this is not a 5 length string!')
        #     continue
        if not matcher.match(guess_str):
            print('please use 5 lowercase letters only!')
            continue
        else:
            x = cows_and_bulls(actual_str, guess_str)
    print("You Win!!!")


game()
#print(cows_and_bulls('abcd', 'acdz'))
#print(cows_and_bulls('abcd', 'abdz'))
#print(cows_and_bulls('aaa', 'aaa'))

