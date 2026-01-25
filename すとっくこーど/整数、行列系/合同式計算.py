#p,a,bは32bitで表せる数の想定

def Mplus(p,a,b) : #a+b
    return (a+b)%p
def Mminus(p,a,b) : #a-b
    return (a-b)%p
def Mtimes(p,a,b) : #a*b
    return (a*b)%p
def gcd(a,b) : 
    AMARI=[]
    AMARI.append(max([a,b]))
    AMARI.append(min([a,b]))
    while AMARI[-1]==0 :
        AMARI.append(AMARI[-2]%AMARI[-1])
    return AMARI[-2]
def lcm(a,b) :
    return int(a*b/gcd(a,b))
def EFA(a,b) : #ax+by=1の解の組を1つ答える
    if a==b :
        return False
    if a==1 :
        return [1,0]
    elif b==1 :
        return [0,1]
    SYO=[]
    AMARI=[]
    V=[1]
    AMARI.append(max([a,b]))
    AMARI.append(min([a,b]))
    while AMARI[-1]!=1 and AMARI[-1]!=0 :
        SYO.append(AMARI[-2]//AMARI[-1])
        AMARI.append(AMARI[-2]%AMARI[-1])
    if AMARI[-1]==0 :
        return False
    else :
        V.append(-SYO[-1])
        for i in range(len(SYO)-1) :
            V.append(V[-2]-V[-1]*SYO[-i-2])
    if a<b :
        return [V[-1],V[-2]]
    elif a>b :
        return [V[-2],V[-1]]
def Minverse(p,a) : #1/a
    return EFA(a,p)[0]%p
def Mdivide(p,a,b) : #a/b
    return (a*Minverse(p,b))%p
def Mpower(p,a,b) : #a**b
    print(0)
for i in range(0) :
    print(1)

