from functools import cmp_to_key
import math
def Syogen(p) :
    #pは2引数タプル
    if p[0]>=0 and p[1]>=0 :
        return 1
    elif p[0]<0 and p[1]>=0 :
        return 2
    elif  p[0]<0 and p[1]<0 :
        return 3
    else :
        return 4
def angle_cmp(p1, p2):
    if Syogen(p1)<Syogen(p2) :
        return -1
    if Syogen(p2)<Syogen(p1) :
        return 1
    cross_product = p1[0] * p2[1] - p1[1] * p2[0]
    if cross_product > 0 :
        return -1
    elif cross_product < 0 :
        return 1
    else :
        return 0

N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))
lst.sort(key=cmp_to_key(arg_sort))
