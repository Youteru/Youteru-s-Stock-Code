#1と-1でないver

H,W=map(int,input().split())
maze = [list(map(int, input().split())) for i in range(H)]

#反転したいもの
A=0
B=1

for i in range (H) :
    j=(i+1)%2
    while j<W :
        if maze[i][j]==A :
            maze[i][j]=B
        elif maze[i][j]==B :
            maze[i][j]=A
        j+=2
print(maze)
