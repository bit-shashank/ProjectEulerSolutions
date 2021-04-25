#############################################################
#                                                           #
# Problem Statement : https://projecteuler.net/problem=011  #
#                                                           #
# ###########################################################



grid=[]
for i in range(20):
    row=[int(i) for i in input().split(" ")]
    grid.append(row)


print(grid)
maxp=-1
for i in range(16):
    for j in range(16):
        hori= grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        vert=grid[j][i]*grid[j][i+1]*grid[j][i+2]*grid[j][i+3]
        diaM=grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        diaS=grid[i+3][j]*grid[i+2][j+1]*grid[i+1][j+2]*grid[i][j+3]
        maxp=max(maxp,hori,vert,diaM,diaS)

print(maxp)