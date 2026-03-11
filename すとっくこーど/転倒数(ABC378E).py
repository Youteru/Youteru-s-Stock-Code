N,M=map(int,input().split())
A=list(map(int,input().split()))
S=[0]
for i in range(N) :
    S.append((S[-1]+A[i])%M)
ans=0
for i in range(N+1) :
    ans+=(-N+2*i)*S[i]
N+=1
####ここが転倒数パート(Sに対して、count=(i<j S[i]>S[j]となる個数)
def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1            # 見つからなかった場合
def compression(data) :
    V=data.copy()
    V=sorted(V)
    last="^o^"
    E=[]
    F=[]
    for i in range(len(V)):
        if V[i]!=last :
            E.append(V[i])
        last=V[i]
    for i in range(len(V)) :
        F.append(binary_search(E,data[i])+1)
    return  F
F=compression(S)
class BIT:
    def __init__(self, N):
        self.N = N
        self.bits = [0] * (self.N + 1)

    #このupdateは加算であることに注意
    def update(self, i, x):
        while i <= self.N:
            self.bits[i] += x
            i += i & -i
    
    def total(self, i):
        res = 0
        
        while i > 0:
            res += self.bits[i]
            i -= i & -i
            
        return res

bits = BIT(N+1)
count = 0
for i in range(N - 1, -1, -1):
    if S[i]>=1 :
        count += bits.total(F[i]-1)
    bits.update(F[i],1)
####
print(ans+count*M)
