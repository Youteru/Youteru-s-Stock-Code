import time

start = time.time()  # 現在時刻（処理開始前）を取得

# 実行したい処理を記述

end = time.time()  # 現在時刻（処理完了後）を取得

time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
print(time_diff)  # 処理にかかった時間データを使用
