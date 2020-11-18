t=int(input())
count=0
for t in range(t):
    n=list(map(int,input().split()))[:3]
    if sum(n)>1:
        count+=1
print(count)




















# n = [1,21,3,14,5,60,7,6]
# k = 81

# d={}
# for i in n:
#     if k-i in n :
#          print(i,k-i)

# for i in n:
#     if k-i in d:
#         print(i,k-i)
#     else:
#         d[i]=i
# print(d)


import math
# mul=0
# for i in range(len(n)):
#     mul=math.prod()
# print(n)
