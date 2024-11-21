a, K, N = map(int, input().split())
start = K - (a % K)
end = N - a
ans = []
for i in range(start, end + 1, K):
    ans.append(i)
if(len(ans) == 0): print(-1)
else:
    for i in ans: print(i, end = " ")
    print()