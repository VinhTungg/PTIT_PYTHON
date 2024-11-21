def nt(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(n):
    if not nt(len(n)): return "NO"
    ngto = 0
    knt = 0
    for i in n:
        if i == '2' or i == '3' or i == '5' or i == '7': ngto += 1
        else: knt += 1
    return "YES" if ngto > knt else "NO"

for _ in range(int(input())):
    n = input()
    print(check(n))