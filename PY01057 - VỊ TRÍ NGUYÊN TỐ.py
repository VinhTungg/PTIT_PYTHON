from math import sqrt

def nt(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def check(n):
    for i in range(len(n)):
        if nt(i) and not nt(int(n[i])): return "NO"
        if not nt(i) and nt(int(n[i])): return "NO"
    return "YES"

for _ in range(int(input())):
    n = input()
    print(check(n))