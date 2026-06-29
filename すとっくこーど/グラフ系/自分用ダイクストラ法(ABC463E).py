import heapq
N,M,Y=map(int,input().split())
PT=[[] for i in range(N+2)]
PC=[[] for i in range(N+2)]
for i in range(M) :
    u,v,T=map(int,input().split())
    u-=1
    v-=1
    PT[u].append(v)
    PT[v].append(u)
    PC[u].append(T)
    PC[v].append(T)
X=list(map(int,input().split()))
PT[N].append(N+1)
PC[N].append(Y)
for i in range(N) :
    PT[i].append(N)
    PT[N+1].append(i)
    PC[i].append(X[i])
    PC[N+1].append(X[i])

#PT,PCを受け取り、頂点Xから各頂点の距離の最小値を求めよう
def Dijkstra(PT,PC,X) :
    N=len(PT)
    INF=10**18
    KA=[False]*N
    ans=[INF]*N
    ans[X]=0
    CM=[]
    heapq.heappush(CM,(ans[X],X))
    while len(CM)>=1 :
        i=heapq.heappop(CM)[1]
        if KA[i] :
            continue
        KA[i]=True
        for j in range(len(PT[i])) :
            k=PT[i][j]
            t=PC[i][j]
            if ans[k]>ans[i]+t :
                ans[k]=ans[i]+t
                heapq.heappush(CM,(ans[k],k))
    return ans
ans=Dijkstra(PT,PC,0)
for i in range(1,N) :
    print(ans[i],end=" ")
print()
       
