isPrime = [True] * 1000005

def sieve():
    for i in range(2, 1001):
        if isPrime[i]:
            for j in range(i * i, 1000001, i):
                isPrime[j] = False

Primes = []
sieve()
for i in range(2, 1000001):
    if isPrime[i]:
        Primes.append(i)

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in Primes:
        if i > n - 6: break
        if isPrime[i + 6] and (isPrime[i + 2] or isPrime[i + 4]):
            cnt += 1
    print(cnt)