


# import math
# n,m=map(int,input().split())
#
# print(n+math.floor((n-1)//(m-1)))

#
# t=int(input())
# for t in range(t):
#     n,m=map(int,input().split())
#
#     while(m!=0):
#         n=n-m
#         m=m//2
#     if n>0:
#         print(0)
#     else:
#         print(1)

# t=int(input())
# for t in range(t):
#     n,m=map(int,input().split())
#     s=list(map(int,input().split()))
#     s.sort(reverse=True)
#     flag=0
#     for i in s:
#         if m%i==0:
#             print(i)
#             flag=1
#             break
#     if flag==0:
#         print(-1)
#
# def count(a):
#     count=0
#     count+=a//9
#     if a%9 == 0:
#         count = count
#     else:
#         count += 1
#     return (count)
# t=int(input())
# for t in range(t):
#
#     c,r=map(int,input().split())
#
#     ccount=count(c)
#     rcount=count(r)
#     if ccount>rcount:
#         print(1,rcount)
#     elif ccount<rcount:
#         print(0,ccount)
#     else:
#         print(1,1)
#






#
# s="daehabshatorawy"
# p="badawy"
#
# s=list(s)
# p=list(p)
#
# for i in p:
#     s.remove(i)
# print(s)
# s.sort()
# print(s)
# print(p)
# print(ord(p[0]))
#
# for i in range(len(s)):
#     if ord(s[i])>ord(p[0]):
#         s.insert(i,("".join(str(i) for i in p)))
#         break
# print(s)
# print("".join(str(i) for i in s))
#












#
# t = int(input())
# for t in range(t):
#     s = list(input())
#     p = list(input())
#     # si=s
#     # s = list(s)
#     # #print(s)
#     # p = list(p)
#     # #print(p)
#     for i in p:
#         s.remove(i)
#     s.sort()
#     # print(s)
#     if len(s) == 0:
#         print(s)
#     else:
#         for i in range(len(s)):
#             if ord(s[i]) > ord(p[0]) :
#                 #print(s[i],p[i],i)
#                 s.insert(i,("".join(str(i) for i in p)))
#                 break
#             elif i+1 == len(s):
#                 s.append("".join(str(i) for i in p))
#                 break
#
#         print("".join(str(i) for i in s))
#     print(s)
#     if p[0] in s:
#         print(s.index(p[0]))
#








# aaaaaaaaxyzaaaaaaaaabbbbbbbbb
# yz



# zzzety
# ze











# s="akramkeeanany"
# p="aka"
# s="akramkeeanany"
# p="aka"
# # s="bca"
# # p="a"
#
# s="a"
# p="a"
# s=list(s)
# p=list(p)
# for i in p:
#     s.remove(i)
# s.sort()
# print(s)
# l=s[:]
# print(l)
#
# l.append(p[0])
# l=sorted(l,reverse=True)
# print("10",l)
# print(l.index(p[0]))
# if p[0] not in s:
#     print("201","".join(s[0:len(l) - l.index(p[0])-1]) + "".join(p)+"".join(s[len(l)-l.index(p[0])-1:]))
#     print("1",s[0:len(l) - l.index(p[0])-1])
#     print("2",s[len(l)-l.index(p[0])-1:])
# else:
#     ps="".join(s[0:s.index(p[0])])+"".join(p)+"".join(s[s.index(p[0]):])
#     print(ps)
#     print("".join(s[0:len(l) - l.index(p[0]) - 1]) + "".join(p) + "".join(s[len(l) - l.index(p[0]) - 1:]))
#     print("1-",s[0:len(l) - l.index(p[0])-1])
#     print("2-",s[len(l)-l.index(p[0])-1:])
#     print("101",min("".join(s[0:len(l) - l.index(p[0])-1]) + "".join(p)+"".join(s[len(l)-l.index(p[0])-1:]),ps))




































# t=int(input())
# for t in range(t):
#
#     string=input()
#     pattern=input()
#
#     string=list(string)
#     pattern=list(pattern)
#     # print(string,pattern)
#
#     for i in range(len(pattern)):
#         string.remove(pattern[i])
#     # print(pattern[0])
#
#     string.sort()
#
#     # print(string)
#
#     if pattern[0] in string and p[-1] in :
#             string.insert(string.index(pattern[0]),"".join(str(i) for i in pattern))
#             #print(string)

    # else:
    #     print("stupid")







#
# s=list("akraamkeeanany")
# p=list("aka")
#
# for i in p:
#     s.remove(i)
# print("beforSort",s)
# s.sort()
# print("Sorted",s)
#
# for i in range(len(s)-1):
#     if p[0] == s[i] and p[-1]<s[i+1]:
#         s.insert(i,"".join(p))
#         print(s)
#         break
#     else:
#         if ord(s[i]) > ord(p[0]):
#             s.insert(i,("".join(str(i) for i in p)))
#             print(s)
#             break



# ['a', 'aka', 'a', 'e', 'e', 'k', 'm', 'n', 'n', 'r', 'y']








# aabbcc==>abcc
# ab
# ==
# aabbcc

# zzzza
# za
# zazzz

#
# from collections import  Counter
# t=int(input())
# for t in range(t):
#     a,k=map(int,input().split())
#     n=list(map(int,input().split()))[:a]
#     d=dict(Counter(n))
#     print(max(d.values())+k)
# # print(d)




# n=['a', 'a', 'e', 'h', 'h', 'o', 'r', 's', 't']
# k=["b","a","d","a","w","y"]
# count=0
# for i in n:
#     if i<k[0]:
#         count+=1
#     else:
#         break
# print(count)
# print("a">"b")
# print("a"<"b")














#
# t=int(input())
# for t in range(t):
#     a=int(input())
#     n=list(map(int,input().split()))
#
#     count=0
#
#     for i in range(len(n)):
#         for j in range(i,len(n)):
#
#             #print(n[i],n[j],i,j,n[i]&n[j])
#             if (n[i]&n[j])==n[i] and i!=j:
#                 count+=1
#     print(count)


s="RLUDRLUD"
s=list(s)

a,b=1,2

x,y=2,3

countleft,countright=0,0
countup,countdown=0,0


for i in s:
    if i=="R":
        countright+=1
    elif i=="L":
        countleft+=1
    elif i=="U":
        countup+=1
    else:
        countdown+=1
print(countright,countleft,countup,countdown)








