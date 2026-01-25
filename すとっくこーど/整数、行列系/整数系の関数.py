def gcd(a,b) : 
    AMARI=[]
    AMARI.append(max([a,b]))
    AMARI.append(min([a,b]))
    while AMARI[-1]!=0 :
        AMARI.append(AMARI[-2]%AMARI[-1])
    return AMARI[-2]
def lcm(a,b) :
    return int(a*b/gcd(a,b))
def HSC(n,p) : #Hyperbola Square Count O(√n)
    X=0
    for i in range(1,math.isqrt(n)+1) :
        X+=(n//i)%p
    return (2*X-(math.isqrt(n))**2)%p
A=int(input())
B=int(input())
print(gcd(A,B))
print(lcm(A,B))
