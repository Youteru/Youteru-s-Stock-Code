#https://zenn.dev/kiwamachan/articles/37a2c646f82c7d
from  collections import deque
N,W=map(int,input().split())
INF = 10**18
A=list(map(int,input().split()))
S=0
for i in range(len(A)):
    S+=A[i]
table=[[0 for j in range(N+2)] for i in range(N+2)]
for i in range(1,N+1) :
    w=list(map(int,input().split()))
    for j in range(1,len(w)) :
       table[i][w[j]]=INF
for i in range(1,N+1) :
    table[0][i]=W
    table[i][N+1]=A[i-1]
# 頂点間ネットワークの初期設定です。
def BFS(v):
    level[v] = 0
    q=deque()
    q.append(v)

    while q:
        v = q.popleft()
        for u in range(N+2):
            if level[u] < 0 and table[v][u] > 0:
                level[u] = level[v] + 1
                q.append(u)
def DFS(fr,flw):
    if fr == N+1:
        return flw
    
    for to in range(N+2):
        if table[fr][to] > 0 and level[fr] < level[to]:
            Dflw = DFS(to,min(flw,table[fr][to]))
            if Dflw > 0:
                table[fr][to] -= Dflw
                table[to][fr] += Dflw
                return Dflw
    return 0
MaxFlw = 0
while True:
    level = [-1]*(N+2)
    BFS(0)
    if level[N+1] < 0 : break

    while True:
        df = DFS(0,INF)
        if df > 0:
            MaxFlw += df
        else:
            break
print(S-MaxFlw)
