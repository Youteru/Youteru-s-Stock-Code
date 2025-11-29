def gcd(a,b) : 
    AMARI=[]
    AMARI.append(max([a,b]))
    AMARI.append(min([a,b]))
    while AMARI[-1]!=0 :
        AMARI.append(AMARI[-2]%AMARI[-1])
    return AMARI[-2]
def lcm(a,b) :
    return int(a*b/gcd(a,b))
A=int(input())
B=int(input())
print(gcd(A,B))
print(lcm(A,B))
