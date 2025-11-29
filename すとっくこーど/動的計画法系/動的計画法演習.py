N=int(input())
A=list(map(int,input().split()))

DP=[0]*(N)

DP[0]=A[0]
DP[1]=max([A[1],A[0]])
for i in range (N-2) :
    DP[i+2] = max([DP[i+1],A[i+2]+DP[i]])
print(DP)
print(DP[-1])
