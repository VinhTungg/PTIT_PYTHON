from math import gcd

class fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def Simplify_numerator(self):
        return self.numerator // gcd(self.numerator, self.denominator)
    def Simplify_denominator(self):
        return self.denominator // gcd(self.denominator, self.numerator)

frac = input().split()
ans = fraction(int(frac[0]), int(frac[1]))
print(f"{ans.Simplify_numerator()}/{ans.Simplify_denominator()}")