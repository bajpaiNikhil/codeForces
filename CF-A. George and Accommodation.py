


t=int(input())
count=0
for t in range(t):
    a,b=map(int,input().split())

    if abs(a-b)>=2:
        count+=1

print(count)





# n=int(input())
#
# l=[]
#
# while(n!=1):
#     l.append(n)
#     if n%2==0:
#         n=n//2
#     else:
#         n=(n*3)+1
# l.append(1)
# print(str(l)[1:-1].replace(",",""))


n=int(input())
arr=list(map(int,input().split()))[:n]
m=len(arr)
sumarr=sum(arr)

d=m*(m+1)//2
print(m)
print(sumarr)
print(d)

print(d-sumarr)


# from collections import  Counter
#
# t=int(input())
# for t in range(t):
#     n=int(input())
#     s=input()[:n]
#     d=dict(Counter(s))
#     flag=0
#     for key,val in d.items():
#         if val%2!=0:
#             flag=1
#             break
#     if flag==1:
#         print("NO")
#     else:
#         print("YES")


#n=[12, 32, 45, 23, 47]
# from functools import reduce
# n=[1,2,7]
# d=[]
# l=[]
# res=0
#
# for i in range(len(n)+1):
#     d.append(n[:i])
#     print(d)
#
#     l.append(reduce(lambda x,y: x or y ,d))
# print(l)

# from functools import reduce
# t=int(input())
# for t in range(t):
#     a=int(input())
#     n=list(map(int,input().split()))[:a]
#     l=[]
#     flag=0
#     for i in range(len(n)+1):
#         for j in range(i+1,len(n)+1):
#             sub=n[i:j]
#             res=reduce(lambda x,y,:x|y,sub)
#             if res not in l:
#                 l.append(res)
#             else:
#                 print("NO")
#                 flag=1
#                 break
#         if flag == 1:
#             break
#     if flag==0:
#         print("YES")

