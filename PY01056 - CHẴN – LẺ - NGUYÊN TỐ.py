from math import sqrt

def nt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return  False
    return n > 1

def check(n):
    for i in range(len(n)):
        if i % 2 == 0 and int(n[i]) & 1: return "NO"
        if i & 1 and int(n[i]) % 2 == 0: return "NO"
    n = int(n)
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return "YES" if nt(ans) else "NO"

for _ in range(int(input())):
    n = input()
    print(check(n))