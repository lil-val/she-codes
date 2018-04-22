def exp(base, ex):
# takes in a base and an exp and recursively computes base**exp. You are not allowed to use the ** operator!
    if ex == 0:
        return 1
    else:
        return base * exp(base, ex - 1)


print(exp(2, 3))
print(exp(3, 0))
print(exp(0, 5))
