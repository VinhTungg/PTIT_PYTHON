def check(s, x):
    for i in range(len(s) - 1):
        if abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(x[i]) - ord(x[i + 1])): return "NO"
    return "YES"


for _ in range(int(input())):
    s = input()
    x = s[::-1]
    print(check(s, x))