

n=int(input())
arr=list(map(int,input().split()))[:n]

if arr.count(1)>=1:
    print("HARD")
else:
    print("EASY")