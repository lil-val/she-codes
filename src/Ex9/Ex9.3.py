def plus_one(digits):
    x = 0
    result = []
    for n in digits:
        x = 10 * x + n
    x += 1
    while x > 0:
        result.append(x % 10)
        x = x // 10
    return result[::-1]


print(plus_one([1, 1]))
print(plus_one([9, 9]))

