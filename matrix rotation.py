matrix = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
l=len(matrix)


c=0
while c<6 :
    new = [[0] * l for _ in range(l)]
    for i in range(l):#0,1,2
        for j in range(l):#0,1,2 repetitive
            new[i][j] = matrix[l - 1 - j][i]

    if new == target:
        print(True)
        break
    c+=1
    matrix = new

print(False)


# for i in range(l):
#     for j in range(l):
#         print(new[i][j],end="\t")
#     print(end="\n")


