




# from collections import Counter
# n=[1,2,4,2]
# d=dict(Counter(n))
# l=[]
# print(d)
#
# for key,val in d.items():
#     if key!=0:
#         while(val>=0):
#             l.append("a"*key)
#             val-=1
#     else:
#         for i in range(val):
#             l.append(chr(98+i))
#
# print(l)

















# t=int(input())
# for t in range(t):
#     s=int(input())
#     n=list(map(int,input().split()))
#     l=[]
#     c=max(n)
#     d=n.count(c)
#     for i in range(s):
#         if n[i]==c:
#             while d>=0:
#                 l.append(chr(97)*n[i])
#                 d-=1
#         elif n[i]==0:
#             l.append(chr(98+i))
#         else:
#             l.append(chr(97)*n[i])
#     # print(len(set(l)))
#     print(l
#           )
#     if len(set(l))!=1:
#         for i in l:
#             print(i,end=" ")
#             print()
#     else:
#         for i in range(s+1):
#             print(chr(97+i))





#
# import sys
# input=sys.stdin.readline
#

# t=int(input())
# for t in range(t):
#     al=int(input())
#     a=list(map(int,input().split()))[:al]
#     maxele=max(a)
#     n=len(a)
#     l=['a' * (maxele+1)] * (n+1)
#     for i ,x in enumerate(a):
#         # print(l[i])
#         altele='a' if l[i][x]=='b' else 'b'
#         l[i+1]=l[i][:x] + altele+l[i][x+1:]
#     print("\n".join(l))

# t=int(input())
#
# for t in range(t):
#     n,m=map(int,input().split())
#     l=list(map(int,input().split()))[:n]
#     s=''
#     for i in l:
#         if i%m==0:
#             s=s+'1'
#         else:
#             s=s+'0'
#     print(s)


# t=int(input())
# for t in range(t):
#     n,m,x,y=map(int,input().split())
#     if n%2!=0 and m%2!=0:
#
#         d=(((n*m)//2)+1)*x
#
#         if abs(y-x)>=x:
#             f=((n*m)//2)*x
#         else:
#             f = ((n * m) // 2) * (abs(y - x))
#         print(d+f)
#     else:
#         d=((n*m)//2)*x
#         if abs(y-x)>=x:
#             f=((n*m)//2)*x
#         else:
#             f = ((n * m) // 2) * (abs(y - x))
#         print(d+f)






