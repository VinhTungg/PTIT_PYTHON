for _ in range(int(input())):
    n = int(input())
    ans = 1
    while n:
        ans *= 1 if n % 10 == 0 else n % 10
        n //= 10
    print(ans)