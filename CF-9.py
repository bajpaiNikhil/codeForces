
n=input()

count1=0
count2=0
count3=0

s=""
for i in n:
    if i =="1":
        count1+=1
    elif i=="2":
        count2+=1
    elif i=="3":
        count3+=1
# print(count1,count2,count3)
for j in range(count1):
    s=s+"1+"
for jj in range(count2):
    s=s+"2+"
for jjj in range(count3):
    s=s+"3+"
print(s[:-1])
