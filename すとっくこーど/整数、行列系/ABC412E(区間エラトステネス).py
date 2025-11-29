import math
def erato(m,n,Plist):
    is_prime = [True] * ((n-m)+1)
    for v in range(len(Plist)):
        i=Plist[v]
        if i*i > n:
            break
        for k in range(i*(math.ceil(m/i)), n+1, i):
            is_prime[k-m] = False
    for i in range(len(Plist)) :
        x=Plist[i]
        while x<=n :
            if x>=m :
                is_prime[x-m]=True
            x=x*Plist[i]
    return is_prime
def eratosthenes2(n):
    is_prime = ([False, True] * (n//2+1))[0: n+1]
    is_prime[1] = False
    is_prime[2] = True
    Plist=[2]
    for i in range(3, n+1, 2):
        if not(is_prime[i]):
            continue
        if i*i > n:
            break
        for k in range(i*i, n+1, i):
            is_prime[k] = False
    for i in range(1,n) :
        if is_prime[i] :
            Plist.append(i)
    return Plist
L,R=map(int,input().split())
if L==R :
    print(1)
else :
    Primer=eratosthenes2(math.ceil(R**(1/2)))
    Table=erato(L,R,Primer)
    ans=1
    for i in range(1,len(Table)) :
        if Table[i] :
            ans+=1
    print(ans)
