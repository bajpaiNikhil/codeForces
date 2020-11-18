



n=int(input())
sum=0
array=list(map(int,input().split()))[:n]
for i in array:
    sum+=i/100


g=(sum/n)*100

print(float("{0:.8f}".format(g)))
