N,S=map(int,input().split())
A=list(map(int,input().split()))

T=[[False] *S]*N


T[0][0]=True

for i in range (N-1) :
    for j in range (S) :
        if j<A[i+1] :
            T[i+1][j] = T[i][j]
        else :
            T[i+1][j]=T[i][j] or T[i][j-A[i+1]]
if T[-1][-1] :
    print(True)
else :
    print(False)
