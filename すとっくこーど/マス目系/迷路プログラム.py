H,W=map(int,input().split())
maze = [list(map(int, input().split())) for i in range(H)]

#道、壁がなにかを定義する。

LOAD=0
WALL=9

#探索関数：ゴールしたらそのときの位置・移動数を返す
def Maze(start):
    #スタート位置（x座標, y座標, 移動回数）をセット
    pos = start

    while len(pos) > 0:#探索可能ならTrue
        x, y, depth = pos.pop(0) #リストから探索する位置を取得

        #ゴールについた時点で終了
        if x==goal[0][0] and y==goal[0][1] :
            return depth

        #探索済みとしてセット
        maze[x][y] = "2"

        #現在位置の上下左右を探索：〇<2は壁でもなく探索済みでもないものを示す
        if maze[x-1][y] == LOAD:#左
            pos.append([x-1, y, depth + 1])
        if maze[x+1][y] == LOAD:#右
            pos.append([x+1, y, depth + 1])
        if maze[x][y-1] == LOAD: #上
            pos.append([x, y-1, depth + 1])
        if maze[x][y+1] == LOAD:#下
            pos.append([x, y+1, depth + 1])
            
    return False

start = [[1, 1, 0]]     #スタート位置
goal = [[3,3,0]]
result = Maze(start)  #探索

print(result)
