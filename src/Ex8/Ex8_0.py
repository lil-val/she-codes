def error(num):
    if num == 0:
        return 1
    else:
        return num * error(num + 1)


print(error(5))
