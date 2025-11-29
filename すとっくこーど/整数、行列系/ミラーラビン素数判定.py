import random

#負の数を入力するとabs(n)までの素数を列挙する
n=int(input())
def miller_rabin(n: int, k: int=3) -> bool:
    if not isinstance(n, int) and not isinstance(k, int):
        raise ValueError("Expect integer number")

    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False

    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    if n < 4759123141 :
        Table=[2,7,61]
    else :
        Table=[2,3,5,7,11,13,17]
    if n in Table :
        return True
    for i in range(len(Table)):
        a = Table[i]
        x = a ** d % n
        if x == 1: continue
        for _ in range(s):
            if x == n-1: break
            x = x**2 % n
        else:
            return False
    return True

#n < 341,550,071,728,321の範囲

def rekkyo(n) :
    for i in range (n) :
        if miller_rabin(i,7) :
            print (i)
#素数を列挙


if n>0 :
    print(miller_rabin(n,7))
else :
    rekkyo(-n)
