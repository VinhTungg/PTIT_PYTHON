for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i, x in enumerate(a):
        if i >= d:
            print(x, end = ' ')
    for i, x in enumerate(a):
        if i < d:
            print(x, end = ' ')
    print()