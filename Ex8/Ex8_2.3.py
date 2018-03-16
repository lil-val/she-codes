def count_down(n):
    #using recursion to print numbers from n to 0
    if n == 0:
        return 0
    elif n < 0:
        print(n)
        return count_down(n + 1)
    else:
        print(n)
        return count_down(n - 1)


print(count_down(5))
print(count_down(0))
print(count_down(-4))
