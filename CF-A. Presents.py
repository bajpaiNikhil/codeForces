

n=int(input())
l=list(map(int,input().split()))
nl=[]
for i in  range(n-1):
    nl[l[i]-1]=i+1
for ti in nl:
    print(ti)