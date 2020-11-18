
# matrix=[[0, 0 ,0 ,0 ,0],
#         [0, 0, 0 ,0 ,1],
#         [0, 0, 0 ,0 ,0],
#         [0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0]]

#print(list(matrix))



import numpy as np
# matrix=[]
# for i in range(5):
#     matrix.append(list(map(int,input().split())))
#print(matrix)

# flatList=np.ravel(matrix)
#
# d=list(flatList).index(1)
#
# # if d==11:
# #     print(0)
#
# print(abs(d-12)%5)

row,col=5,5
a=[]
for i in range(1,row+1):
    for j in range(1,col+1):
        a[i][j]=int(input())

        if a[i][j]==1:
            print(abs(i-3)+abs(j-3))
            break
