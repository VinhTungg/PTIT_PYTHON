ok = 0
def check(s):
    for i in s:
        if (i == 4 or i == 7): ok = 1
        else : ok = 0

test = int(input())
while(test):
    num = input()
    if (ok): print("YES")
    else: print("NO")