#AとBの最長共通部分列の長さを出力する
def LCS(A,B) :
    if len(A)==0 or len(B)==0 :
        return 0
    else :
        H=len(A)+1
        W=len(B)+1
        T=[[0 for j in range(W)] for i in range(H)]
        for i in range(1,H) :
            for j in range(1,W) :
                if A[i-1]==B[j-1] :
                    T[i][j]=max(T[i-1][j-1]+1,T[i-1][j],T[i][j-1])
                else :
                    T[i][j]=max(T[i-1][j],T[i][j-1])
        return T[-1][-1]
N=int(input())
S=input()
S=S+"#"
ans=0
X=0
for i in range(N) :
    if S[i]==S[i+1] :
        X=1
        A=S[0:i][::-1]
        B=S[i+2:N]
        ans=max(ans,2+2*LCS(A,B))
    A=S[0:i][::-1]
    B=S[i+1:N]
    ans=max(ans,1+2*LCS(A,B))
print(ans)
