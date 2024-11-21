def check(a, b):
    for i, val in enumerate(a):
        if val > b[i]: return "NO"
    return "YES"

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print(check(a, b))