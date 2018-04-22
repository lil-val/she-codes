# Ex 1
myfunction(x, y):  # def is missing
    return x + y

else:  # there is no if before the else
    print("Hello!")

if mark >= 50  # : is missing
    print("You passed!")

if arriving:
    print("Hi!")
esle:  # typo in else
    print("Bye!")

if flag:
print("Flag is set!")  # the print statement should be indented
#  ***************************************************************

# Ex 2
dividend = float(input("Please enter the dividend: "))
divisor = float(input("Please enter the divisor: "))
quotient = dividend / divisor
quotient_rounded = math.round(quotient)

"""
the inserted values may not be int or float and may not be converted to float (e.g. str may be inserted)
the value of the divisor may be set to zero
math should be imported
"""
#  *******************************************************************

#  Ex 3
for x in range(a, b):
    print("(%f, %f, %f)" % my_list[x])

"""
a, b, and my_list are not defined
the range between a to b may be bigger from the length of my_list, in this case index [x] may not be part of my_list
as per the formatting the length of the list is 3, however the list may be shorter or bigger
"""
#  *********************************************************************

#  Ex 4
product = 0
for i in range(10):
    product *= i

sum_squares = 0
for i in range(10):
    i_sq = i**2
sum_squares += i_sq

nums = 0
for num in range(10):
    num += num

"""
product should be equal to 1 and not zero, if product = 0 the value of product will remain zero
sum_squares should be indented and be inside the for loop
in line 56 nums should be used instead of num
"""





