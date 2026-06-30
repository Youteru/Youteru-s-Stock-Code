#ゼータ変換、メビウス変換のライブラリを作ります

def FZT(A) :
    N=len(A).bit_length()-1
    assert len(A)==1<<N
    for i in range(N) :
        for t in range(1<<N) :
            if (t>>i) & 1 :
                A[t]+=A[t^(1<<i)]
    return A
def FMT(A) :
    N=len(A).bit_length()-1
    assert len(A)==1<<N
    for i in range(N-1,-1,-1) :
        for t in range((1<<N)-1,-1,-1) :
            if (t>>i)&1 :
                A[t]-=A[t^(1<<i)]
    return A
#一瞬でライブラリ作れた
