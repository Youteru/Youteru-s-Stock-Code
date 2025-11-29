import math

H,W=map(int,input().split())
maze = [list(map(int, input().split())) for i in range(H)]

#各マスは -1 か 1　でできている。
#x座標とy座標の和が奇数のマスを反転する

for i in range (H) :
    j=(i+1)%2
    while j<W :
        maze[i][j]=-maze[i][j]
        j+=2

print(maze)


