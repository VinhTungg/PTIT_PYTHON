t = int(input())
for i in range(t):
    s = input()
    i = 0
    while(i < len(s)):
        cnt = 1
        tmp = i
        while(tmp < len(s) - 1 and s[tmp] == s[tmp + 1]):
            cnt += 1
            tmp += 1
        print(f"{cnt}{s[i]}", end = '')
        i = tmp + 1
    print()
