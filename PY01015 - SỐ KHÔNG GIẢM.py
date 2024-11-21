def check(n):
    for i in range(1, len(n)):
        if(n[i - 1] > n[i]): return "NO"
    return "YES"

t = int(input())
for i in range(t):
    n = input()
    print(check(n))