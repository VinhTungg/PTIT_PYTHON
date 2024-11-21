def solve(n):
    sum = 0
    while(n > 9):
        du = n % 10
        sum += du
        n //= 10
        if(abs(du - n % 10) != 2): return "NO"
    sum += n
    if(sum % 10 == 0): return "YES"
    return "NO"

t = int(input())
for i in range(t):
    n = int(input())
    print(solve(n))