#ダブリングです
#A=[f(0),f(1),,,,,f(N-1)]に対して、A^nを出力します。
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
A=list(map(int,input().split()))
N=len(A)
