def lam_tron(n):
    p = 10
    while n >= p:
        n = (n + p // 2) // p * p
        p *= 10
    return n

t = int(input())
while t:
    n = int(input())
    print(lam_tron(n))
    t -= 1