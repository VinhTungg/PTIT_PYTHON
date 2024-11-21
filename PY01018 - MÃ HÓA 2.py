P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while (1):
    tmp = input()
    if(tmp[0] == "0"): break
    k , s = tmp.split()
    k = int(k)
    ans = ""
    for i in s:
        ans += P[(P.index(i) + k) % 28]
    print(ans[::-1])