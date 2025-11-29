N=int(input())
#一つ入力
A=list(input())
#文字列を一文字ずつ区切ってリスト化
A=list(map(int, input().split()))
#空白で区切られた複数入力(リスト)
H, W = map(int, input().split())
#空白で区切られた複数入力(変数)
A = [list(input()) for i in range(N)]
#長さNの改行で区切られた複数入力(リスト)
A=[0 for i in range(N)]
#N個要素持つ0リスト
A=[[0 for i in range(W)]for j in range(H)]
#W*Hの0平面リスト
for j in range (N) :
    print(A[j],end=" ")
#空白で区切る出力
A = [list(map(int, input().split())) for i in range(H)]
#空白、改行で区切られた平面リスト
    
       
