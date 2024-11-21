t = int(input())
for i in range(t):
    n = int(input())
    print(1, end = '')
    j = 2
    while j * j <= n:
        cnt = 0
        while(n % j == 0):
            cnt += 1
            n //= j
        if(cnt): print(f" * {j}^{cnt}", end = '')
        j += 1
    if(n > 1): print(f" * {n}^{1}", end = '')
    print()