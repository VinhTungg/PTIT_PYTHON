t = int(input())
for _ in range(t):
    sum = int(input())
    cnt = 0
    while sum % 7:
        sum += int(str(sum)[::-1])
        cnt += 1
        if(cnt == 1000): break
    if cnt <= 1000: print(sum)
    else: print(-1)