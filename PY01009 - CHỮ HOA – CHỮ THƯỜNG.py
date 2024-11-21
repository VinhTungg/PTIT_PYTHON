s = input()
hoa, thuong = 0, 0
for i in s:
    if(i.isupper()): hoa += 1
    else: thuong += 1
if(hoa <= thuong): print(s.lower())
else : print(s.upper())