




a=input()

ded=0
rota=0
flag=97
for i in a:
    ded=abs(flag-ord(i))
    if ded>13:
        ded=26-ded
    rota+=ded
    flag=ord(i)
print(rota)