from math import sqrt

def check(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    tmp = 0
    while n:
        tmp += n % 10
        n //= 10
    print(check(tmp))