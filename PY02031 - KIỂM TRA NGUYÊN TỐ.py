def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return n > 1

n, m = map(int, input().split())

a = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for idx, num in enumerate(tmp):
        if isprime(num):
            tmp[idx] = 1
        else: tmp[idx] = 0
    a.append(tmp)

for arr in a:
    print(*arr)