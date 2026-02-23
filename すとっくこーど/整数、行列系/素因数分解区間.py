from math import isqrt
def ERA(N) :
    ans=[[] for i in range(N+1)]
    D=[i for i in range(N+1)]
    is_prime = ([False, True] * (N//2+1))[0: N+1]
    for i in range(2,N+1,2) :
        t=(i & -i).bit_length() - 1
        ans[i].append((2,(i & -i).bit_length() - 1))
        D[i]//=2**t
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, isqrt(N)+1,2):
        if not(is_prime[i]):
            continue
        for k in range(i*i, N+1, i):
            is_prime[k] = False
            v=k
            c=0
            ans[k].append((i,1))
            D[k]//=i
        for k in range(i*i, N+1, i*i):
            v=k
            c=0
            while v%i==0 :
                v=v//i
                c+=1
            del ans[k][-1]
            ans[k].append((i,c))
            D[k]//=i**(c-1)
    for i in range(1,N+1) :
        if D[i]>1 :
            ans[i].append((D[i],1))
    return ans
N=int(input())
A=list(map(int,input().splt()))
