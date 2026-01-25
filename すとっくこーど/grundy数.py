#サブトラクションセットSを、有限集合と、自然数M以上の全ての自然数の和集合とした場合、
#グランディ数は規則的な振る舞いをしますか。------>Yes

#サブトラクションセットSに対するグランディ数g(X)を計算する
#現実的には|S|=2ならmaxS<=2^63でも、|S|=3ならmaxS<=10000,|S|=4ならmaxS<=100
#Sの総積が10**16以下なら余裕とされている
#option="A"ならX以下全て出力する
#option="C"ならサイクルの長さを、option="P"ならサイクルに入るまでの長さを計算する
#サイクル検出にハッシュを用いようと思ったが実装がめちゃくちゃだるいと分かった
#Lは実行回数の限界、通常10^7
def grundy(S,X,option,L) :
    ans=0
    pre=0
    cycle=0
    MAX=max(S)
    MIN=min(S)
    D=3*(MAX**(len(S)-1))
    if X*len(S)<=L or option="A":
        G=[0 for i in range(MIN)]
        for i in range(MIN,X+1) :
            Y=0
            K=set()
            for j in range(len(S)) :
                K.add(G[i-S[j]])
            while Y in K :
                Y+=1
            G.append(Y)
    else :
        G=[0 for i in range(MIN)]
        for i in range(MIN,D+1) :
            Y=0
            K=set()
            for j in range(len(S)) :
                K.add(G[i-S[j]])
            while Y in K :
                Y+=1
            G.append(Y)
            
    if option==None :
        return G[X]
    elif option=="A" :
        return G
print(grundy([2,3],20,None,10**8))
    
