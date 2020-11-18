

# s="abcdefg"
# t="AbCdEfF"
from collections import Counter
s=input().lower()
t=input().lower()

if s<t:
    print(-1)
elif t<s:
    print(1)
else:
    print(0)











# Ssum=0
# Tsum=0
# ds=Counter(s)
# ts=Counter(t)
# print(ds)
# print(ts)
#
# #print(list(ds.keys())[1])
# #print(ord(ds[1]))
#
# for i in range(len(s)-1):
#     if (ord(list(ds.keys())[i])) < (ord(list(ts.keys())[i])) :
#         print(-1)
#         break
#     elif (ord(list(ds.keys())[i])) < (ord(list(ds.keys())[i])):
#         print(1)
#         break
# print(0)
#
# # for i in s.lower():
# #     Ssum+=ord(i)
# # print(Ssum)
# # for j in t.lower():
# #     Tsum+=ord(j)
# # print(Tsum)
# # if Ssum<Tsum:
# #     print("-1")
# # elif (Tsum<Ssum):
# #     print(1)
# # else:
# #     print(0)