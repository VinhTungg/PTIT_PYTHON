def check(n):
    return "YES" if n % 3 == 0 else "NO"

for _ in range(int(input())):
    n = int(input())
    tmp = 0
    while n:
        tmp += n % 10
        n //= 10
    print(check(tmp))