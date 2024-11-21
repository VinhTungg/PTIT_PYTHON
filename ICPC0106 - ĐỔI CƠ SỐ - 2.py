import math
def base16(n):
    if n == 10: return 'A'
    elif n == 11: return 'B'
    elif n == 12: return 'C'
    elif n == 13: return 'D'
    elif n == 14: return 'E'
    elif n == 15: return 'F'

for _ in range(int(input())):
    n = int(input())
    s = input()
    if(n == 2): print(s)
    else:
        n = math.log(n, 2)
        cnt, sum = 0, 0
        s = s[::-1]
        ans = ""
        for i, val in enumerate(s):
            cnt += 1
            if(val == '1'): sum += 2 ** (i % int(n))
            if(cnt == int(n)):
                if(sum > 9): sum = base16(sum)
                ans += str(sum)
                sum = 0
                cnt = 0
        if(sum): ans += str(sum)
        print(ans[::-1])
