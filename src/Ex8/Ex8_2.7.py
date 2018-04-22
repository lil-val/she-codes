def fibonacci(n):
    # takes in one argument n and computes Fn, the nth value of the Fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4))
print(fibonacci(7))
