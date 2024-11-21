def check(n):
    return "YES" if n == n[::-1] and len(n) > 1 else "NO"

for _ in range(int(input())):
    n = int(input())
    tmp = 0
    while n:
        tmp += n % 10
        n //= 10
    print(check(str(tmp)))