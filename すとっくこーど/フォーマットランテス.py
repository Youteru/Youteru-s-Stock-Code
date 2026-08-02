#問題:1<=x<y<=Nとなる(x,y)はいくつあるか

N=int(input())
K=N*(N-1)//2
print(K)

#→

import random

def IP() :
    N=int(input())
    return N

def RIP() :
    N=random.randint(1,1000)
    
def solve() :
    K=N*(N-1)//2
    print(K)

def test() :
    ans=0
    for x in range(N) :
        for y in range(x+1,N) :
            ans+=1
    print(ans)

def main() :
    
    #スイッチ装置1
    """
    N=IP()
    """
    N=RIP()

    #スイッチ装置2
    """
    solve(N)
    """
    print()
    solve()
    test()

#スイッチ装置3
"""
main()
"""
for i in range(100) :
    main()
