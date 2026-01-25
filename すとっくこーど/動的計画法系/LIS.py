#最長増加部分列の長さを出力する
def LIS(A) :
    N=len(A)
    L=[10**10 for i in range(N+1)]
    L.append(-100)
    L.append(-100)
    for i in range(N) :
        Y=A[i]
        right=N
        left=0
        while left<right-1 :
            mid=(left+right)//2
            if L[mid]>=Y :
                right=mid
            else :
                left=mid
        if L[left-1]>=Y :
            mid=left-1
        elif L[left]>=Y :
            mid=left
        elif L[left+1]>=Y :
            mid=left+1
        else :
            mid=left+2
        L[mid]=Y
    for i in range(N+1) :
        if L[i]==10**10 :
            return i
def LDS(A) :
    return LIS(list(reversed(A)))
print(LDS([1,2,3,1,2,3,1,2,3]))
