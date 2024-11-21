from math import gcd

n = int(input())

a = list(map(int, input().split()))
a.sort()
for i, num in enumerate(a):
    for j in range(i + 1, len(a)):
        if gcd(num, a[j]) == 1:
            print(num, a[j])