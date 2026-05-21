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
#これは事故らない二分探索です
def binary_min(data, lower_bound):
    value=lower_bound
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left < right:
        mid = (left + right) // 2# 探索する範囲の中央を計算
        if data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid +1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid
    mid = (left + right) // 2
    return mid            # 見つからなかった場合
#これは事故らない二分探索です
def binary_max(data, upper_bound):
    value=upper_bound
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left < right:
        mid = (left + right+1) // 2# 探索する範囲の中央を計算
        if data[mid] > value:
            # 中央の値より大きい場合は探索範囲の左を変える
            right = mid -1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            left = mid
    mid = (left + right) // 2
    return mid            # 見つからなかった場合
def compression(A) :
    S = sorted(list(set(A))) ## [4, 8, 25, 30, 90]
    ranking = {x:i for i,x in enumerate(S)} ## {4: 1, 8: 2, 25: 3, 30: 4, 90: 5}
    A_zaatsu = []
    for a in A:
      A_zaatsu.append(ranking[a])
    return  A_zaatsu
N=int(input())
A=list(map(int,input().split()))
Q=int(input())
A=sorted(A)
for q in range(Q) :
    b=int(input())
    X=binary_min(A,b)
    Y=binary_max(A,b)
    print(min(abs(A[X]-b),abs(A[Y]-b)))
