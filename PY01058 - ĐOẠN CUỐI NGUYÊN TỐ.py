def nt(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return "NO"
    return "YES" if n > 1 else "NO"

for _ in range(int(input())):
    print(nt(int(input()[-4:])))