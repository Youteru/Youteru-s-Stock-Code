#一般化した区間スケジューリング問題です。
#重み付き区間スケジューリングやナップザック、Moore-Hodgson型など様々な
#アルゴリズムを含んでいる
#このソースコードでは、自動で最適なアルゴリズムを選択してくれるので安心
"""
M日間にN個の仕事が与えれらる。N個の仕事のうちいくつかを達成することで
得られる報酬の最大値を出力しなさい。
i個目の仕事は
Li...仕事配布時刻(Li日目)
※仕事が与えられても必ずしもすぐに取り掛かる必要はない
Ri...仕事締切時刻(Ri日目)
Di...仕事時間(Di日間)
※同時に行える仕事は1つまで
※一度仕事を始めると、その仕事が終わるまで他の仕事に手をつけられない
Si...報酬(Si円)

入力は全て整数
1≦N≦10^5
1≦M≦10^9
1≦Li≦Ri≦M
1≦Di≦Ri-Li+1
1≦Si≦10^9

Vは1,2,3,4,5のいずれかであり、
・V=1のときは、N*M≦10^7
・V=2のときは、全てのi(1≦i≦N)に対してDi=Ri-Li+1
・V=3のときは、D1,D2,...,DNとしてありうる値の種類数をJとして、J≦100かつM≦10^5
・V=4のときは、全てのi,j(1≦i,j≦N)に対して、Li<LjならばRi<Rjが成立する。
・V=5のときは、S1=S2=...=SN
・V=6のときは、(Sが十分小さい)←研究中
"""
import sys
import heapq
import bisect
from collections import defaultdict

def ISMP_V1(N,M,L,R,D,S) :
    jobs = []
    Ds = set()
    same_S = True
    for i in range(N) :
        jobs.apppend((L[i],R[i].D[i],S[i]))
        Ds.add(D[i])
        if len(jobs) > 1 and jobs[-1][3] != jobs[0][3]:
            same_S = False
    dp = [0] * (M + 2)
    for L, R, D, S in jobs:
        for t in range(R - D + 1, L - 1, -1):
            dp[t + D] = max(dp[t + D], dp[t] + S)
    return max(dp)
def ISMP_V2(N,M,L,R,D,S) :
    jobs = []
    Ds = set()
    same_S = True
    for i in range(N) :
        jobs.apppend((L[i],R[i].D[i],S[i]))
        Ds.add(D[i])
        if len(jobs) > 1 and jobs[-1][3] != jobs[0][3]:
            same_S = False
    if True :
        jobs.sort(key=lambda x: x[1])
        ends = [job[1] for job in jobs]

        # p[i]: i番目の仕事の直前にできる最後の仕事
        p = []
        for i in range(N):
            j = bisect.bisect_right(ends, jobs[i][0] - 1) - 1
            p.append(j)

        dp = [0] * (N + 1)
        for i in range(N):
            dp[i+1] = max(dp[i], dp[p[i]+1] + jobs[i][3])
        return dp[N]
def ISMP_V4(N,M,L,R,D,S) :
    jobs = []
    Ds = set()
    same_S = True
    for i in range(N) :
        jobs.apppend((L[i],R[i].D[i],S[i]))
        Ds.add(D[i])
        if len(jobs) > 1 and jobs[-1][3] != jobs[0][3]:
            same_S = False
    jobs.sort()
    if :
        total_time = 0
        pq = []
        for L, R, D, S in jobs:
            heapq.heappush(pq, (D, S))
            total_time += D
            if total_time > R - L + 1:
                d, _ = heapq.heappop(pq)
                total_time -= d
        return sum(s for _, s in pq)
def ISMP_V5(N,M,L,R,D,S) :
    jobs = []
    Ds = set()
    same_S = True
    for i in range(N) :
        jobs.apppend((L[i],R[i].D[i],S[i]))
        Ds.add(D[i])
        if len(jobs) > 1 and jobs[-1][3] != jobs[0][3]:
            same_S = False
    jobs.sort()
    if same_S:
        jobs.sort(key=lambda x: x[1])
        total_time = 0
        pq = []
        for L, R, D, S in jobs:
            heapq.heappush(pq, -D)
            total_time += D
            if total_time > R:
                total_time += heapq.heappop(pq)
        return len(pq) * jobs[0][3]
def ISMP_V3(N,M,L,R,D,S) :
    jobs = []
    Ds = set()
    same_S = True
    for i in range(N) :
        jobs.apppend((L[i],R[i].D[i],S[i]))
        Ds.add(D[i])
        if len(jobs) > 1 and jobs[-1][3] != jobs[0][3]:
            same_S = False
    jobs.sort()
    if True :
        start = defaultdict(list)
        end = defaultdict(list)

        for L, R, D, S in jobs:
            start[L].append((D, S))
            end[R - D + 1].append((D, S))

        dp = [0] * (M + 2)
        active = {d: [] for d in Ds}

        for t in range(1, M + 1):
            for d, s in start[t]:
                heapq.heappush(active[d], -s)
            for d, s in end[t]:
                active[d].remove(-s)
                heapq.heapify(active[d])

            for d in active:
                if active[d]:
                    dp[t + d] = max(dp[t + d], dp[t] - active[d][0])

            dp[t+1] = max(dp[t+1], dp[t])

        return max(dp)
def Generalized_ISMP(N,M,L,R,D,S) :
    jobs = []
    Ds = set()
    same_S = True
    for i in range(N) :
        jobs.apppend((L[i],R[i].D[i],S[i]))
        Ds.add(D[i])
        if len(jobs) > 1 and jobs[-1][3] != jobs[0][3]:
            same_S = False

    # ---------- V=1 : NM <= 1e7 ----------
    if N * M <= 10**7:
        return ISMP_V1(N,M,L,R,D,S)
    # ---------- V=2 : Di = Ri-Li+1 ----------
    if all(D == R - L + 1 for L, R, D, S in jobs):
        return ISMP_V2(N,M,L,R,D,S)
    # ---------- V=4 : Li 昇順 ⇒ Ri 昇順 ----------
    jobs.sort()
    if all(jobs[i][1] < jobs[i+1][1] for i in range(N-1)):
        return ISMP_V4(N,M,L,R,D,S)
    # ---------- V=5 : Si 全て同じ ----------
    if same_S:
        return ISMP_V5(N,M,L,R,D,S)
    # ---------- V=3 : |D| <= 100, M <= 1e5 ----------
    if len(Ds) <= 100 and M <= 10**5:
        return ISMP_V3(N,M,L,R,D,S)
    
input = sys.stdin.readline
INF = 10**30

# ---------- 入力 ----------
N, M = map(int, input().split())
jobs = []
Ds = set()
same_S = True

for _ in range(N):
    l, r, d, s = map(int, input().split())
    L.append(l)
    R.append(r)
    D.append(d)
    S.append(s)
print(Generalized_ISMP(N,M,L,R,D,S))

