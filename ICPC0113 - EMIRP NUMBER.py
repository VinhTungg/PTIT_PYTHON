import math

def tn(n):
    m = 0
    while n > 0:
        a = n % 10
        m = m * 10 + a
        n //= 10
    return m

def prime(n):
    if n < 2: return 0
    for i in range(2, int(math.sqrt(n))+1, 1):
        if(n % i == 0): return 0
    return 1

t = int(input())
while t:
    res = {}
    n = int(input())
    for i in range(13, n+1):
        if(prime(i)):
            if not i in res:
                rev = tn(i)
                if(rev in res or i in res): continue
                maxNum = max(i, rev)
                if(prime(rev) and maxNum < n and maxNum != i):
                    print(i, rev, end = ' ')
                res[rev] = res[i] = 1
    print()
    t -= 1