def check(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

for _ in range(int(input())):
    n = input()
    dau = n[:3]
    cuoi = n[-3:]
    print("YES" if check(int(cuoi)) and check(int(dau)) else "NO")