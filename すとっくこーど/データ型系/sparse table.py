import sys
import random
#★3以下を埋めていこう
def func(x,y) :
    return min(x,y)
class SparseTable :
    def __init__(self,init_val,func) :
        self.func=func
        self.n=len(init_val)
        self.depth = (self.n - 1).bit_length()
        self.table=init_val+[0]*(self.n*(self.depth-1))
        for d in range(self.depth-1) :
            for i in range(self.n-(1<<d)) :
                self.table[(d+1)*self.n+i]=self.func(self.table[d*self.n+i],self.table[d*self.n+i+(1<<d)])
    # [l,r)でクエリ実行
    def query(self,l,r) :
        if r-l==1 :
            return self.table[l]
        self.level = (r-l- 1).bit_length() - 1
        return self.func(self.table[self.level*self.n+l], self.table[self.level*self.n+r - (1<<self.level)])
#ランダムテスト
Q=50
N=1000
A=[random.randint(1,1000000000) for i in range(N)]
spa=SparseTable(A,func)
for i in range(Q) :
    l,r=sorted([random.randint(0,N),random.randint(0,N)])
    print(min(A[l:r]),spa.query(l,r))
