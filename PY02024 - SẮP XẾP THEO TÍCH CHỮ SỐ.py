def custom_key(n):
    sum = 1
    while n > 0:
        sum *= n % 10
        n = n // 10
    return sum

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x: (custom_key(x), x))
    for x in a:
        print(x, end = " ")
    print()