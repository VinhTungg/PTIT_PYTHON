def fibo(n, m):
    res = []
    f1, f2 = 1, 1
    for i in range(0, m):
        res.append(f1)
        f1, f2 = f2, f1 + f2
    return res

t = int(input())
while t:
    a, b = map(int, input().split())
    res = fibo(a, b)
    a -= 1
    b -= 1
    for i, j in enumerate(res):
        if i >= a:
            print(j, end = ' ')
        elif i > b: break
    print()
    t -= 1