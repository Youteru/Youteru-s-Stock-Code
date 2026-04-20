#覚えておくべきユニコード一覧
#文字列を処理する問題は、文字列を全て数に置き換えると高速化できる
"""
最重要(覚えておけ)
35 #
40 (
41 )
46 .
65-90 A-Z
97-122 a-z

重要でない
32 空白
33 !
42 *
43 +
45 -
47 /
48-57 0-9
60 <
61 =
62 >
63 ?
"""
def nth_alpha(n) :
    print(chr(n+97))
def nth_Alpha(n) :
    print(chr(n+65))
def alpha_nth(s) :
    print((ord(n)-65)%32)

#と.でできた写真を1と0に変換する
def picture_bit(x) :
    A=[]
    for p in x :
        A.append(list(map(ord,list(p))))
        for i in range(len(p)) :
            A[-1][i]%=2
    return A
print(picture_bit(["##.#","...#"]))
