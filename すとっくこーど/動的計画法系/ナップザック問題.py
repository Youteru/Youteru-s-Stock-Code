#入力は N target value weight　の順番
N=int(input())
target=int(input())
value=list(map(int,input().split()))
weight=list(map(int,input().split()))

# 重さと値段を保存するクラスを作成
class Item:
    def __init__(self, w=0, p=0):
        self.weight = w
        self.price = p

# 配列にして保存する。
items=[]
for i in range (N) :
    items.append(Item(value[i],weight[i]))

dp = [[[]for i in range(target+1)] for j in range(len(items)+1)]
memo = []


def serachNum(i,j):
    target = j
    num = i - 1
    # 現在の値
    weight = items[num].weight
    price = items[num].price

    while True:
        # ここの処理は変更していない。
        memo.append(weight)
        if weight == target:
            break
        elif target<weight:
            weight -= items[num].weight
            price -= items[num].price
            num -= 1
            if num == -1:
                break
            else:
                weight += items[num].weight
                price += items[num].price
        else:
            num -=1
            if num == -1:
                break
            else:
                weight += items[num].weight
                price += items[num].price


    print("値:",price,"重さ：",weight,)


    return price





# ナップサックの処理(一応DP)
def knapsack():
    # 初期値の設定
    weight = 0
    value = 0
    M_value = 0

    for i in range(len(items)+1):
        for j in range(target+1):
            # 0行目
            if i == 0:

                if j == 0:
                    # 0列目
                    dp[i][j] = 0
                else:
                    dp[i][j] = "INF"

            else:
                if j == 0:
                    # 配列0列目
                    dp[i][j] = 0
                else:
                    # 配列1個目以降
                    # 一つ前のコインの組み合わせ方を取得
                    # 今回求めたコインの組み合わせを取得
                    comparison = dp[i - 1][j]
                    ans = serachNum(i, j)

                    if type(comparison) == int:
                        if ans > comparison:
                            # 今回の組み合わせが最短手だった時
                            dp[i][j] = ans
                        else:
                            # 前回以前の組み合わせが最短手だった時
                            dp[i][j] = comparison

                    else:
                        # 一つ前の最善手が数字ではないとき
                        dp[i][j] = ans


knapsack()
