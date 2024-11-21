import math

def nt(n):
    n = int(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1

def check(n):
    if not nt(len(n)): return "NO"
    cnt = 0
    for i in n:
        if nt(int(i)): cnt += 1
    return "YES" if cnt > len(n) - cnt else "NO"

for _ in range(int(input())):
    n = input()
    print(check(n))