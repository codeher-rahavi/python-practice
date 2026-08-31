matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
zeroth_place = []
row=len(matrix)
col=len(matrix[0])


dummy_matrix = [[0]*col for _ in range(row)]

for i in range(row):
    for j in range(col):
        print(dummy_matrix[i][j],end="\t")
    print(end="\n")

print()

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end="\t")
    print(end="\n")

print()

for i in range(row):
    for j in range(col):
        if matrix[i][j] ==0:
            zeroth_place.append((i,j))
            dummy_matrix[i][j] = -1


for i in range(row):
    for j in range(col):
        print(dummy_matrix[i][j],end="\t")
    print(end="\n")



print(zeroth_place)






