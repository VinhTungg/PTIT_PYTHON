import math

def nt(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0: return False
    return n > 1

def check(n, m):
    uoc = math.gcd(n, m)
    tong = 0
    while uoc:
        tong += uoc % 10
        uoc //= 10
    if(nt(tong)): return True
    return False

t = int(input())
while t:
    n, m = map(int, input().split())
    if(check(n, m)): print('YES')
    else: print('NO')
    t -= 1