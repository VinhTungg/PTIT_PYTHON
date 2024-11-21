from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def Simplify(self):
        self.numerator //= gcd(self.numerator, self.denominator)
        self.denominator //= gcd(self.denominator, self.numerator)
    def add(self, other):
        numerator1 = self.numerator * other.denominator
        numerator2 = self.denominator * other.numerator
        sum_denominator = self.denominator * other.denominator
        self.numerator = (numerator1 + numerator2) // gcd(numerator1 + numerator2, sum_denominator)
        self.denominator = sum_denominator // gcd(numerator1 + numerator2, sum_denominator)
        return f"{self.numerator}/{self.denominator}"

num = input().split()

frac1 = Fraction(int(num[0]), int(num[1]))
frac2 = Fraction(int(num[2]), int(num[3]))
print(frac1.add(frac2))