#クエリ j: 頂点 A_jから B_jまで、辺を向きのとおりに通って移動することは可能か？
#そういうクエリを判定する問題です
import heapq
import sys

from atcoder.scc import SCCGraph

#PTは矢印の行き先、FTは矢印の戻り先、NNは頂点数
def minTPS(PT,FT,NN) :
  CM=[]
  heapq.heapify(CM)
  FTC=[len(FT[i]) for i in range(NN)]
  res=[]
  for i in range(NN) :
    if FTC[i]==0 :
      heapq.heappush(CM,i)
  for i in range(NN) :
    x=heapq.heappop(CM)
    res.append(x)
    for k in PT[x] :
      FTC[k]-=1
      if FTC[k]==0 :
        heapq.heappush(CM,k)
  return res
def maxTPS(PT,FT,NN) :
  CM=[]
  heapq.heapify(CM)
  FTC=[len(FT[i]) for i in range(NN)]
  res=[]
  for i in range(NN) :
    if FTC[i]==0 :
      heapq.heappush(CM,-i)
  for i in range(NN) :
    x=-heapq.heappop(CM)
    res.append(x)
    for k in PT[x] :
      FTC[k]-=1
      if FTC[k]==0 :
        heapq.heappush(CM,-k)
  return res
def main() -> None:
    N,M,Q = map(int, sys.stdin.readline().split())
    g = SCCGraph(N)
    W=[]
    for i in range(M):
        u, v = map(int, sys.stdin.readline().split())
        u-=1
        v-=1
        W.append((u,v))
        g.add_edge(u, v)

    scc = g.scc()
    A=[0 for i in range(N)]
    i=0
    for c in scc:
        for x in c:
            A[x]=i
        i+=1
    for i in range(M) :
      W[i]=(A[W[i][0]],A[W[i][1]])
    W=set(W)
    NN=len(scc)
    for i in range(NN) :
      W.discard((i,i))
    W=list(W)
    PT=[[] for i in range(NN)]
    FT=[[] for i in range(NN)]
    for u,v in W :
      PT[u].append(v)
      FT[v].append(u)
    B=minTPS(PT,FT,NN)
    C=maxTPS(PT,FT,NN)
    D=[0 for i in range(NN)]
    E=[0 for i in range(NN)]
    for i in range(NN) :
      D[B[i]]=i
      E[C[i]]=i
    B=D.copy()
    C=E.copy()
    for i in range(Q) :
      a,b=map(int,input().split())
      a-=1
      b-=1
      if B[A[a]]<=B[A[b]] and C[A[a]]<=C[A[b]] :
        print("Yes")
      else :
        print("No")
if __name__ == '__main__':
    main()
