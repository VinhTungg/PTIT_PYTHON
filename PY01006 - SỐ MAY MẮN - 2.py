def check(n):
    for i in n:
        if(i == '4' or i == '7'): continue
        else: return "NO"
    return "YES"

t = int(input())
while t:
    s = input()
    print(check(s))
    t -= 1
