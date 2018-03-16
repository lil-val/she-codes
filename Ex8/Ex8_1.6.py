def sum(n):
    #Write a function sum that takes a single argument n and computes the sum of all integers between 0 and n inclusive. Assume n is non-negative
    if n == 1:
        return 1
    else:
        return sum(n - 1) + n


print(sum(5))
print(sum(1))
