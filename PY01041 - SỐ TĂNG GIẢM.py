def check(s):
    if(len(s) < 3): return "NO"
    for i in range(len(s) - 1):
        if(s[i] < s[i + 1]):
            for j in range(i, len(s)):
                if(j == len(s) - 1): return "YES"
                if(s[j] <= s[j + 1]): break
        else :
            for j in range(i, len(s)):
                if(j == len(s) - 1): return "YES"
                if(s[j] <= s[j + 1]): break
            return "NO"

for _ in range(int(input())):
    s = input()
    print(check(s))