

#from  more_itertools import unique_everseen

t=int(input())

for i in range(t):
    a=int(input())
    n=list(map(int,input().split()))[:2*a]
    # l=list(unique_everseen(n))
    # print(str(l)[1:-1].replace(",",""))
    d=list(dict.fromkeys(n))
    print(str(d)[1:-1].replace(",",""))
