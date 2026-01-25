#p,a,bは32bitで表せる数の想定
import math
import sys
def Mplus(p,a,b) : #a+b
    return (a+b)%p
def Mminus(p,a,b) : #a-b
    return (a-b)%p
def Mtimes(p,a,b) : #a*b
    return (a*b)%p
def gcd(a,b) :
    a=abs(a)
    b=abs(b)
    AMARI=[]
    AMARI.append(max([a,b]))
    AMARI.append(min([a,b]))
    while AMARI[-1]!=0 :
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
    m=p
    p = a
    answer = 1
    for i in range(math.floor(math.log2(b))+1) :
    	if (b & (1 << i)) != 0:
    		answer = (answer * p) % m
    	p = (p * p) % m
    return answer
def base_10(n,m): #m進数のnを10進数にしたものを出力
    num_10 = 0
    for s in str(n):
        num_10 *= m
        num_10 += int(s)
    return num_10
def base_m(num_10,m): #10進数のnum_10をm進数にする、勝手にアルファベットを使用する
    str_n = ''
    while num_10:
        if num_10%m>=36:
            return -1
        elif num_10%m>=10:
            str_n +=chr(num_10%m+87)
        else :
            str_n += str(num_10%m)
        num_10 //= m
    return str_n[::-1]
def baselist_p(n,p) : #10進数のnをp進数でリストにする
    list_n=[]
    while n :
        list_n.append(n%p)
        n=n//p
    return list_n
def Mfact(p,a) :
    ans=1
    for i in range(1,a+1) :
        ans=(ans*i)%p
    return ans
#aCb計算パート
M=10
p=998244353
t=1
FP=[0 for i in range(M)] # i番目はi!%p
FI=[0 for i in range(M)] # i番目は(1/i!)%p
for i in range(1,M+1) :
    t=(t*i)%p
    FP[i-1]=t
FI[-1]=Minverse(p,FP[-1])
for i in range(M-2,-1,-1) :
    FI[i]=(FI[i+1]*(i+2))%p
FP=[1]+FP
FI=[1]+FI
#########
def C(p,a,b) :
    return (((FP[a]*FI[a-b])%p)*FI[b])%p
#########
MOD=998244353
p=7
print(baselist_p(35,4))
A=int(input())
B=int(input())
print(Mpower(p,A,B))
