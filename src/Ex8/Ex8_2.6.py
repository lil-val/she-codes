def is_prime(n):
    #check if a number n is prime (you have to check whether n is divisible by any number below n).
    if n == 0:
        return False
    if n <= 2:
        return True
    return helper(n, 2)


def helper(n, z):
    if n == z:
        return True
    if n % z == 0:
        return False
    return helper(n, z + 1)


print(is_prime(2))
print(is_prime(5))
print(is_prime(4))
