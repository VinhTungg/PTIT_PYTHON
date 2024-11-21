def check(n):
    for i in n:
        if(i == '0' or i == '1' or i == '2'): continue
        else: return "NO"
    return "YES"

for _ in range(int(input())):
    n = input()
    print(check(n))