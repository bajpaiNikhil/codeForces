


n=input()
lower=0
upper=0
for i in n:
    if i==i.lower():
        lower+=1
    elif i==i.upper():
        upper+=1
#print(lower,upper)

if lower>=upper:
    print(n.lower())
else:
    print(n.upper())
