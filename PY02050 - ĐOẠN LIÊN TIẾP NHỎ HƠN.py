for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    b.append(a[0])
    for i in range(1, n):
        l = r = i
        while l > -1 and a[l] <= a[r]: l -= 1
        print(r - l, end = ' ')