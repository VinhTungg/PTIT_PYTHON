def check(s):
    if(s[:2] == s[-2:]): return "YES"
    else: return "NO"

t = int(input())
while t:
    s = input()
    print(check(s))
    t -= 1