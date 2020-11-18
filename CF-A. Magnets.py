



n=int(input())
s=0
count=0
while(n>0):
    a=int(input())

    if s!=a:
        count+=1
    s=a
    n-=1

print(count)