a,b=map(int,input().split())
l=list(map(int,input().split()))[:a]
count=0
score=l[b-1]
for i in l:
    if i >=score and i>0:
        count+=1
print(count)

