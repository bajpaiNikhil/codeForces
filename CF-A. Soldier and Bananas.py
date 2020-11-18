


k,n,w=map(int,input().split())
#
# l=[3,6,9,12]
# print(sum(l))
l=[]
for i in range(1,w+1):
    l.append(k*i)

#print(sum(l))
if sum(l)<n:
    print(0)
else:
    print(abs(sum(l)-n))

#print(abs(sum(l)-17))

