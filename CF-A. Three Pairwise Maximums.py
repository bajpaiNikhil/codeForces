
from collections import Counter
#n=int(input())
# for i in range(n):
#     x,y,z=map(int,input().split())
#     small=min(x,y,z)
#     large=max(x,y,z)
#     if x==y==z:
#         print("YES")
#         print(x,y,z)
#
#     elif (x==y!=z or x==z!=y or y==z!=x) and (small<large):
#         print("YES")
#         small=min(x,y,z)
#         print(small+1,small,small-1)
#
#     else:
#         print("NO")
#
#
t=int(input())
for t in range(t):
    l=list(map(int,input().split()))[:3]

    l.sort(reverse=True)
    if l[0]==l[1]==l[2]:
        print("YES")
        print(l[0],l[0],l[0])
    elif (l[0]==l[1] and l[0]>l[2]):
        print("YES")
        print(l[0],l[2],l[2])
    else:
        print("NO")
