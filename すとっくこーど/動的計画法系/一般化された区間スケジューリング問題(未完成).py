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
・V=3のときは、N*sumS<=10^7
・V=4のときは、全てのi,j(1≦i,j≦N)に対して、Li<LjならばRi<Rjが成立する。
・V=5のときは、S1=S2=...=SN
・V=6のときは、D1=D2=...=DN=1が成立する

V=1,2,3は完成済み、V=4,5,6は未完成
"""
import sys
import heapq
import bisect
from collections import defaultdict
from random import randint

def ISMP_V1(N,M,L,R,D,S) :
    dp = [0] * (M + 2)
    intervals = []
    for i in range(N) :
        intervals.append((L[i],R[i],D[i],S[i]))
    intervals.sort(key=lambda x: x[1])
    L=[]
    R=[]
    D=[]
    S=[]
    for i in range(N) :
        L.append(intervals[i][0])
        R.append(intervals[i][1])
        D.append(intervals[i][2])
        S.append(intervals[i][3])
    for i in range(N) :
        for t in range(R[i] - D[i] + 1, L[i] - 1, -1):
            dp[t + D[i]] = max(dp[t + D[i]], dp[t] + S[i])
        for x in range(len(dp)-1) :
            dp[x+1]=max(dp[x+1],dp[x])
    return max(dp)
def ISMP_V2(N,M,L,R,D,S) :
#重み付き区間スケジューリング問題むずい
#後で完成させとく

    intervals = []
    for i in range(N) :
        intervals.append((L[i],R[i],S[i]))
    intervals.sort(key=lambda x: x[1])
    # dp[i]: 最初のi個の区間から選んだ最大重み（dp[0]は0）
    dp = [0] * (N + 2)
    end_times=[]
    # 終了時間のリスト（二分探索用）

    for i in range(1, N + 1):
        start, end, weight = intervals[i-1]

        # 1. 区間 i-1 を選ばない場合
        option1 = dp[i-1]

        # 2. 区間 i-1 を選ぶ場合
        # 重複しない直前の区間を探す (終了時間が start-1 以前)
        # bisect_rightで挿入位置を見つけ、その位置の1つ前（-1）が、
        # start よりも前に終わる最大のインデックス
        end_times.append(intervals[i-1][1])
        prev_idx = bisect.bisect_right(end_times, start - 1)
        # prev_idx は 0 から i-1 の範囲で [start-1] が挿入される位置。
        # 実際のインデックスは prev_idx-1。dp配列のインデックスは prev_idx。
        # dp[prev_idx] は、その位置までの最大値。

        option2 = weight + dp[prev_idx]

        dp[i] = max(option1, option2)

    return dp[N]
def ISMP_V3(N,M,L,R,D,S) :
    SS=0
    intervals = []
    for i in range(N) :
        intervals.append((L[i],R[i],D[i],S[i]))
    intervals.sort(key=lambda x: x[1])
    L=[]
    R=[]
    D=[]
    S=[]
    for i in range(N) :
        L.append(intervals[i][0])
        R.append(intervals[i][1])
        D.append(intervals[i][2])
        S.append(intervals[i][3])
    for i in range(N) :
        SS+=S[i]
    dp=[M+100]*(SS+2)
    dp[0]=0
    for i in range(N) :
        for y in range(0,SS+1) :
            x=SS-y
            if max(dp[x], L[i]-1) + D[i] <= R[i] and x+S[i]<=SS+1 :
                new_end = max(dp[x], L[i]-1) + D[i]
                dp[x + S[i]] = min(dp[x + S[i]], new_end)
    for y in range(0,SS+1) :
        x=SS-y
        if dp[x]<=M :
            return x
def ISMP_V4(N,M,L,R,D,S) :
    jobs = []
    Ds = set()
    same_S = True
    for i in range(N) :
        jobs.append((L[i],R[i],D[i],S[i]))
        Ds.add(D[i])
        if len(jobs) > 1 and jobs[-1][3] != jobs[0][3]:
            same_S = False
    jobs.sort()
    if True :
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
        jobs.append((L[i],R[i],D[i],S[i]))
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

def Generalized_ISMP(N,M,L,R,D,S) :
    jobs = []
    Ds = set()
    same_S = True
    for i in range(N) :
        jobs.append((L[i],R[i],D[i],S[i]))
        Ds.add(D[i])
        if len(jobs) > 1 and jobs[-1][3] != jobs[0][3]:
            same_S = False

    # ---------- V=1 : 一般解法　O(NM) ----------
    if N * M <= 10**7:
        return ISMP_V1(N,M,L,R,D,S)
    # ---------- V=2 : Di = Ri-Li+1 O(NlogN)----------
    if all(D == R - L + 1 for L, R, D, S in jobs):
        return ISMP_V2(N,M,L,R,D,S)
    # ----------V=3 : 一般解法　O(NsumS) --------
    if N*sum(S) <= 10**7:
        return ISMP_V3(N,M,L,R,D,S)
    # ---------- V=4 : Li 昇順 ⇒ Ri 昇順 O(NlogN)----------
    jobs.sort()
    if all(jobs[i][1] < jobs[i+1][1] for i in range(N-1)):
        return ISMP_V4(N,M,L,R,D,S)
    # ---------- V=5 : Si 全て同じ O(NlogN)----------
    if same_S:
        return ISMP_V5(N,M,L,R,D,S)

input = sys.stdin.readline
INF = 10**30

# ---------- 入力 ----------
"""
N, M = map(int,input().split())
L=[]
R=[]
D=[]
S=[]
for _ in range(N):
    l,r,s=map(int,input().split())
    L.append(l)
    R.append(r)
    D.append(r-l+1)
    S.append(s)
"""

for _ in range(100) :
    N, M = 5,1000
    L=[]
    R=[]
    D=[]
    S=[]
    for _ in range(N):
        l=randint(1,1000)
        r=randint(l,1000)
        d=randint(1,r-l+1)
        s=randint(1,100)
        L.append(l)
        R.append(r)
        D.append(r-l+1)
        S.append(s)
    print(ISMP_V1(N,M,L,R,D,S),ISMP_V2(N,M,L,R,D,S),ISMP_V3(N,M,L,R,D,S))
