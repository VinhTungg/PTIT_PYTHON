n = int(input())
while n:
    a = []
    a.append(n)
    while n != 1:
        if n & 1: n = n * 3 + 1
        else: n >>= 1
        a.append(n)
    print(len(a))
    n = int(input())