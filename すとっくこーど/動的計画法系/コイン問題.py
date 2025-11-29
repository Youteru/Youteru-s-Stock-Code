n,m=map(int,input().split())
C=list(map(int,input().split()))
inf = 100000

T1 = [[inf for _ in range(n+1)] for __ in range(m)]
for k in range(m):
    T1[k][0] = 0

for i in range(n+1):
    for j in range(m):
        if(i < C[j]):
            T1[j][i] = T1[j-1][i]
        else:
            T1[j][i] = min(T1[j-1][i],T1[j][i-C[j]]+1)


print(T1[-1][-1])

#額面がc1, c2,..., cm　円の　m　種類のコインを使って、
#n 円を支払うときの、コインの最小の枚数を求めて下さい。
#各額面のコインは何度でも使用することができます。
