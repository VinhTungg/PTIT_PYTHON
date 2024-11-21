def tn(num):
    m = 0
    while num:
        a = num % 10
        m = m*10 + a
        num //= 10
    return m

def check(num):
    cnt = 0
    while num:
        a = num % 10
        if a % 2 != 0: return 0
        num //= 10
        cnt += 1
    return (cnt % 2 == 0)

t = int(input())
while t:
    n = int(input())
    for i in range(22, n, 1):
        if (check(i) and i == tn(i)):
            print(i, end = ' ')
            pass
    print()
    t -= 1