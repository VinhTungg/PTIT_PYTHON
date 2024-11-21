def check(n):
    for i in range(len(n) - 2 - (len(n) & 1)):
        if(n[i] != n[i + 2]): return "NO"
    return "YES"

for _ in range(int(input())):
    s = input()
    print(check(s))