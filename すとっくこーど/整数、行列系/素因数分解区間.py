from math import isqrt
#ERA(10**6)で500ms,めっちゃ遅い
#空間的に重いのが原因ですね。
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
#Omega(10**7)で888ms
def omega(N) :
    ans=[(i+1)%2 for i in range(N+1)]
    D=[i for i in range(N+1)]
    is_prime = ([False, True] * (N//2+1))[0: N+1]
    for i in range(2,N+1,2) :
        t=(i & -i).bit_length() - 1
        D[i]//=2**t
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, isqrt(N)+1,2):
        if not(is_prime[i]):
            continue
        for k in range(i*i, N+1, i):
            is_prime[k] = False
            ans[k]+=1
            D[k]//=i
        for k in range(i*i, N+1, i*i):
            v=k
            c=0
            while v%i==0 :
                v=v//i
                c+=1
            D[k]//=i**(c-1)
    for i in range(1,N+1) :
        if D[i]>1 :
            ans[i]+=1
    return ans
print(omega(100))
def Omega(N) :
    ans=[(i & -i).bit_length() - 1 for i in range(N+1)]
    D=[i for i in range(N+1)]
    is_prime = ([False, True] * (N//2+1))[0: N+1]
    for i in range(2,N+1,2) :
        t=(i & -i).bit_length() - 1
        D[i]//=2**t
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, isqrt(N)+1,2):
        if not(is_prime[i]):
            continue
        for k in range(i*i, N+1, i):
            is_prime[k] = False
            ans[k]+=1
            D[k]//=i
        for k in range(i*i, N+1, i*i):
            v=k
            c=0
            while v%i==0 :
                v=v//i
                c+=1
            ans[k]+=c-1
            D[k]//=i**(c-1)
    for i in range(1,N+1) :
        if D[i]>1 :
            ans[i]+=1
    return ans
def div_funk(N) :
    ans=[(i & -i).bit_length() for i in range(N+1)]
    D=[i for i in range(N+1)]
    is_prime = ([False, True] * (N//2+1))[0: N+1]
    for i in range(2,N+1,2) :
        t=(i & -i).bit_length() - 1
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
            while v%i==0 :
                v=v//i
                c+=1
            ans[k]*=c+1
            D[k]//=i**c
    for i in range(1,N+1) :
        if D[i]>1 :
            ans[i]*=2
    return ans
print(div_funk(100))
ERA(10000000)
N=int(input())
A=list(map(int,input().split()))
G=Omega(100000)
ans=0
for i in range(N) :
    ans^=G[A[i]]
if ans==0 :
    print("Bruno")
else :
    print("Anna")
