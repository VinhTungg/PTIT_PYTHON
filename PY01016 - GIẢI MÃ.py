t = int(input())
for i in range(t):
    s = input()
    for j in s:
        if(j.isalpha()): tmp = j
        if(j.isdigit()):
            for i in range(int(j)): print(tmp, end = '')
    print()