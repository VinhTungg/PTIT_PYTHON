for _ in range(int(input())):
    p, q = input().split()
    s1, s2 = input().split()
    s1 = s1.replace(p, q)
    s2 = s2.replace(p, q)
    Num1 = int(s1) + int(s2)
    s1 = s1.replace(q, p)
    s2 = s2.replace(q, p)
    Num2 = int(s1) + int(s2)
    if Num1 > Num2: Num1, Num2 = Num2, Num1
    print(Num1, Num2)