def doubler(A,K) :
    B=[]
    B.append(A)
    for i in range(len(str(bin(K)))) :
        C=[]
        for j in range(len(A)) :
            C.append(B[-1][B[-1][j]])
        B.append(C)
    D=[i for i in range(len(A))]
    for i in range(len(str(bin(K)))) :
        if K%2==1 :
            for j in range(len(A)) :
                D[j]=B[i][D[j]]
        K=K//2
    return D
N,K=map(int,input().split())
A=[]
for i in range(N+1) :
    V=0
    R=i
    for t in range(len(str(N+1))) :
        V+=R%10
        R=R//10
    A.append(i-V)
Ans=doubler(A,K)
for i in range(1,N+1) :
    print(Ans[i])
