def roman_to_int(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums = []
    total = 0
    for char in s:
        nums.append(values[char])
    if len(nums) > 1:
        for num1, num2 in zip(nums, nums[1:]):
            if num1 >= num2:
                total += num1
            else:
                total -= num1
        return total + num2
    else:
        return nums[0]


print(roman_to_int('I'))
print(roman_to_int('III'))
print(roman_to_int('IX'))
print(roman_to_int('XII'))
print(roman_to_int('XCIX'))

