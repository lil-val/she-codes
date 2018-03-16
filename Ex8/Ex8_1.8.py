def hailstone(n):
    #If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. Repeat this process until n is 1.
    # Write a recursive version of hailstone that prints out the values of the sequence and returns the number of steps.
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)


print(hailstone(10))
