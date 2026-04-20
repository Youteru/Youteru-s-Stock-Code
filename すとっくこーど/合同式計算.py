#p,a,bは32bitで表せる数の想定
import math
import sys
from random import randint
def Mplus(p,a,b) : #a+b
    return (a+b)%p
def Mminus(p,a,b) : #a-b
    return (a-b)%p
def Mtimes(p,a,b) : #a*b
    return (a*b)%p

#間違ってないと思う、速くした。
#gcd(|a|,|b|) ただしa=0ならb,b=0ならaを出力する。
#wikiに載っているgcdの定義と同じ
def gcd(a,b) :
    a=abs(a)
    b=abs(b)
    while a>0 and b>0 :
        b%=a
        a,b=b,a
    return max(a,b)
def lcm(a,b) :
    return int(a*b/gcd(a,b))
def sign(x) :
    if x>0 :
        return 1
    elif x==0 :
        return 0
    else :
        return -1

#高速化したもの ax+by=gcd(|a|,|b|)　を解く,a,b!=0に注意!
def EFA(a,b) :
    s=0
    u=abs(b)
    z=abs(a)
    x=a//z
    while z>0 :
        s=s-(u//z)*x
        u=u-(u//z)*z
        x,z,s,u=s,u,x,z
    return (s,(u-a*s)//b)

#EFAを0に対応したもの,ちゃんと動くかはしらん
def EFA2(a,b) :
    s=0
    u=abs(b)
    z=abs(a)
    x=((a<<1)+1)//((z<<1)+1)
    if b==0 :
        return (0,sign(b))
    while z>0 :
        s=s-(u//z)*x
        u=u-(u//z)*z
        x,z,s,u=s,u,x,z
    return (s,(u-a*s)//b)
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
M=2000000
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


