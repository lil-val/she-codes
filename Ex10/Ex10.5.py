def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


class Rational:
    def __init__(self, p, q):  # p = numerator, q = denominator
        if q == 0:
            raise ZeroDivisionError('denominator cannot be zero!')
        else:
            d = greatest_common_divisor(p, q)
            self.p = p / d
            self.q = q / d

    def __str__(self):
        return "%d / %d" % (self.p, self.q)

    def __add__(self, other):
        # add two rational numbers: p1/q1 + p2/q2 = p1*q2 + p2*q1 / q1*q2
        return Rational(self.p * other.q + other.p * self.q, self.q * other.q)

    def __sub__(self, other):
        # subtract two rational numbers: p1/q1 - p2/q2 = p1*q2 - p2*q1 / q1*q2
        return Rational(self.p * other.q - other.p * self.q, self.q * other.q)

    def __mul__(self, other):
        # multiplication of two rational numbers: p1/q1 * p2/q2 = p1*p2 / q1*q2
        return Rational(self.p * other.p, self.q * other.q)

    def __truediv__(self, other):
        # division of two rational numbers: (p1/q1) / (p2/q2) = p1*q2 / p2*q1
        return Rational(self.p * other.q, other.p * self.q)

    # def is_equal(self, other):
    #     #check if two rational numbers are equal
    #     if self.p / self.q == other.p / other.q:
    #         return True
    #     else:
    #         return False

    def __float__(self):
        # return a float number
        return float(self.p) / float(self.q)

    def __eq__(self, other):
        # check if two rational numbers are equal
        if self.p / self.q == other.p / other.q:
            return True
        else:
            return False


r1 = Rational(10, 20)
r2 = Rational(5, 15)
r3 = Rational(2, 6)
r5 = Rational(10, 20)
# r4 = Rational(1, 0)
# print(r4)

print(r1)
print(r2)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)
print(r1 == r2)
print(r1 == r5)
print(r2 == r3)
print(float(r1))
