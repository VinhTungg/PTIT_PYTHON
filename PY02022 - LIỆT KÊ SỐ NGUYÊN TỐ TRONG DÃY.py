def isprime(num):
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0: return False
    return num > 1

n = int(input())
m = []

a = list(map(int, input().split()))
for i in a:
    if isprime(i) and i not in m:
        m.append(i)
        print(i, a.count(i))