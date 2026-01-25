def HLRA(hist):
    target = [0] + hist + [0]
    stack = []
    max_area = 0

    for i, height in enumerate(target):
        while stack and target[stack[-1]] > height:
            h = target[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area
#Aは0と1のみの2次元リストで、内部の数字総和が0になる長方形の面積の最大値を出力する
def LRA(A) :
    H=len(A)
    W=len(A[0])
    RSW=[[0 for j in range(W)] for i in range(H)]
    for j in range(W) :
        C=0
        for i in range(H) :
            if A[H-1-i][j]==1 :
                C=0
            else :
                C+=1
            RSW[i][j]=C
    ans=0
    for i in range(H) :
        ans=max(ans,HLRA(RSW[i]))
    return ans
H,W=map(int,input().split())
A=[]
for i in range(H) :
    A.append(list(map(int,input().split())))
print(LRA(A))
