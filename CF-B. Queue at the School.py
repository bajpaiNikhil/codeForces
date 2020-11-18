


n,m=map(int,input().split())
s=input()[:n]
s=list(s)
#print(s)
d=""
while m>0:
    for j in range(len(s)-1):
        if (s[j]=='B' and s[j+1]=='G'):
            s[j],s[j+1]=s[j+1],s[j]
            j+=1
        j+=1
    m-=1
print(s)

for i in range(len(s)):
    d+=s[i]
print(d)
