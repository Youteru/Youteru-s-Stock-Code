s = input()
t = input()
A,B,C=map(int,input().split())
inf = float("inf")

# 文字の長さに、最初の空白文字の長さを加算する
s_l = len(s) + 1
t_l = len(t) + 1

    # テーブルを作成
dp = [[inf] * s_l for _ in range(t_l)]

    # 1行目を埋める
dp[0] = [B*i for i in range(s_l)]

    # 1列目を埋める
for j in range(t_l):
        dp[j][0] = A*j

    # 2行2列目以降を埋める
for i in range(1, t_l):
        for j in range(1, s_l):
            left = dp[i][j - 1] + B
            upp = dp[i - 1][j] + A
            if s[j - 1] == t[i - 1]:
                left_upp = dp[i - 1][j - 1]
            else:
                left_upp = dp[i - 1][j - 1] + C

            dp[i][j] = min(left, upp, left_upp)

    # t_l, s_lは文字の長さのため、インデックスに変換するために-1を行う
print(dp[t_l - 1][s_l - 1])

#文字列sをtに変換する金額を表す。挿入にA円、削除にB円、置換にC円かかる。
