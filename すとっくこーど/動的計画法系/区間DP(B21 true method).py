N=int(input())
S=input()
ans=0
X=0
DP=[[0 for j in range(N)] for i in range(N)]
for i in range(N) :
    for j in range(0,N-i) :
        L=j
        R=L+i
        if L==R :
            DP[L][R]=1
        else :
            if S[L]==S[R] :
                if L==R-1 :
                    DP[L][R]=2
                else :
                    DP[L][R]=max(2+DP[L+1][R-1],DP[L][R-1],DP[L+1][R])
            else :
                DP[L][R]=max(DP[L][R-1],DP[L+1][R])
print(DP[0][N-1])
            
