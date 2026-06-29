from bisect import bisect_left,bisect_right
#pythonで、「非負整数の単調増加数列Aと非負整数Xが与えられたとき、Aに含まれない非負整数であって、X+1番目に小さいものを求める」関数を作って下さい。高速なアルゴリズムでなければなりません。
#配列Aに含まれない非負整数であって、X番目に小さいものを求めます
#A:ソート済配列
def n_MEX_CK(A,ans,X) :
    Y=bisect_left(A,ans)
    if ans-Y<=X :
        return True
    else :
        return False
def n_MEX(A,X) :
    ans=len(A)+X-1
    D=ans.bit_length()
    for d in range(D+1) :
        if n_MEX_CK(A,ans,X) :
            ans+=2**(D-d)
        else :
            ans-=2**(D-d)
    if not n_MEX_CK(A,ans,X) :
        ans-=1
    return ans
N,M=map(int,input().split())
A=list(map(int,input().split()))
for i in range(N) :
    A[i]-=1
RK=[[] for i in range(N)]
C=[0 for i in range(M)]
for i in range(N) :
    RK[C[A[i]]].append(A[i])
    C[A[i]]+=1
for i in range(N) :
    RK[i]=sorted(RK[i])
RSW=[0]
for i in range(N) :
    RSW.append(RSW[-1]+M-len(RK[i]))
Q=int(input())
for i in range(Q) :
    X=int(input())-1
    if X<N :
        print(A[X]+1)
    elif X-N>=RSW[-1] :
        print(1+(X-N-RSW[-1])%M)
    else :
        k=bisect_right(RSW,X-N)-1
        print(1+n_MEX(RK[k],X-N-RSW[k]))
        
