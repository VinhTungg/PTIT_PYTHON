def check(s):
    if len(s) < 1: return "NO"
    else:
        if s[-2:] == "86": return "YES"
        else: return "NO"

t = int(input())
for i in range(t):
    s = input()
    print(check(s))