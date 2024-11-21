def check(n):
    if not len(n) & 1: return "NO"
    if n[0] == n[1]: return "NO"
    for i in range(0, len(n) - 1, 2):
        if n[i] != n[i + 2]: return "NO"
    return "YES"

for _ in range(int(input())):
    n = input()
    print(check(n))