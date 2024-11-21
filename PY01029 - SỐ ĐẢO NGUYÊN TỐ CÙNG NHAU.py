import math

t = int(input())
for i in range(t):
    n = input()
    num1 = int(n)
    num2 = int(n[::-1])
    print("YES" if math.gcd(num1,num2) == 1 else "NO")