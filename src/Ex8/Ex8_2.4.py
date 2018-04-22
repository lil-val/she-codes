def count_up(n, z):
    #print numbers from 0 to n
    if n == z:
        return z
    elif n < z:
        print(z)
        return count_up(n, z - 1)
    else:
        print(z)
        return count_up(n, z + 1)


print(count_up(4, 0))
print(count_up(0, 0))
print(count_up(-5, 0))
