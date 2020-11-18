

#1 3 5 7 2 4 6


n,k=map(int,input().split())
#n=1,2,3,4,5,6,7,8,9,10

if k<=(n+1)//2:
    print((2*k)-1)
else:
    print(2*(k-((n+1)//2)))