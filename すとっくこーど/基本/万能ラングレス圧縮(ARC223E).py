#この関数はリストでも文字列でも使える
def RLE(s):
    n = len(s) #文字列の長さ
    ans = [] #圧縮後のリスト
    l = 0 #始点
    while l<n:
        r = l+1
        while r<n and s[l]==s[r]: #異なる文字になるまで進む
            r += 1
        ans.append((s[l], r-l)) #文字,連続する個数
        l = r #連続しなかった文字から探索を開始
    return ans
T=int(input())
for t in range(T) :
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    C=[]
    D=[]
    if A[0]!=B[0] :
        print("No")
        continue
    elif A[-1]!=B[-1] :
        print("No")
        continue
    for i in range(N-1) :
        C.append(A[i]^A[i+1])
        D.append(B[i]^B[i+1])
    
