H,W=map(int,input().split())
maze = [list(map(int,input().split())) for i in range(H)]

#枠を付けて地図を作成

maze.insert(0, ["WALL" for j in range (W)])
maze.append(["WALL" for j in range (W)])
for i in range (H+2) :
    maze[i].insert(0,"WALL")
    maze[i].append("WALL")

#面積計測関数：面積とエリアを返す
def AreaResearch(ThisPoint):
    #道がなにかを定義する。
    start = [[ThisPoint[0],ThisPoint[1], 0]] 
    LOAD=maze[ThisPoint[0]][ThisPoint[1]]
    counter=0
    Area=[]
    #スタート位置（x座標, y座標, 移動回数）をセット
    pos = start

    while len(pos) > 0:#探索可能ならTrue
        x, y, depth = pos.pop(0) #リストから探索する位置を取得

        #探索済みとしてセット
        maze[x][y] = "Checked"
        Area.append([x,y])
        counter+=1

        #現在位置の上下左右を探索：〇<2は壁でもなく探索済みでもないものを示す
        if maze[x-1][y] == LOAD:#左
            pos.append([x-1, y, depth + 1])
        if maze[x+1][y] == LOAD:#右
            pos.append([x+1, y, depth + 1])
        if maze[x][y-1] == LOAD: #上
            pos.append([x, y-1, depth + 1])
        if maze[x][y+1] == LOAD:#下
            pos.append([x, y+1, depth + 1])
            
    return [counter,Area]


ThisPoint=[1,2] #調査位置(入力)<----壁つけた関係で１つずれてます

result = AreaResearch(ThisPoint)  #探索
print(result)
