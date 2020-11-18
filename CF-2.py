

t=int(input())

for t in range(t):
    n=str(input())
    s=len(n)
    if len(n)>10:
        print(n[0]+str(s-2)+n[-1])
    else:
        print(n)
