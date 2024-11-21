import math

n, m = map(int, input().split())
for i in range(n, m - 1):
    for j in range(i + 1, m):
        for k in range(j + 1, m + 1):
            if math.gcd(i, k) == 1 and math.gcd(j, k) == 1 and math.gcd(i, j) == 1:
                print(f'({i}, {j}, {k})')