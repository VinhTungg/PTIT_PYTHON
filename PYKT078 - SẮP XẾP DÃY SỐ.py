for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b, c = [], []
    tmp = max(a)
    for i in a:
        if i < 0:
            if i == tmp:
                b.append(m)
                b.append(i)
                tmp = 1e10
            else:
                b.append(i)
        else:
            if i == tmp:
                c.append(m)
                c.append(i)
                tmp = 1e10
            else:
                c.append(i)
    for i in b: print(i, end=' ')
    for i in c: print(i, end=' ')
    print()