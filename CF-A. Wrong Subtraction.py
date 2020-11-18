

n,k=map(int,input().split())
# print(n%10)
while(k>0):
    #print(n)
    if (n%10) == 0:
        n=n//10
    else:
        n=n-1
    k-=1
    #print(k)
print(n)