class BalancingTree:
    def __init__(self, n):
        self.N = n
        self.root = self.node(1<<n, 1<<n)

    def append(self, v):# v を追加（その時点で v はない前提）
        v += 1
        nd = self.root
        while True:
            if v == nd.value:
                # v がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p&-p)//2)
                        break
                else:
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p&-p)//2)
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v): # vより真に小さいやつの中での最大値（なければ-1）
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v): # vより真に大きいやつの中での最小値（なければRoot）
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1<<self.N)-1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd = None, prev = None): # 値がvのノードがあれば削除（なければ何もしない）
        v += 1
        if not nd: nd = self.root
        if not prev: prev = nd
        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    #####
                    return
            else:
                if nd.right:
                    nd = nd.right
                else:
                    #####
                    return
        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right = None
            elif not prev.right:
                prev.left = None
            else:
                if nd.pivot == prev.left.pivot:
                    prev.left = None
                else:
                    prev.right = None

        elif nd.right:
            # print("type A", v)
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd)    
        else:
            # print("type B", v)
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd)

    def __contains__(self, v: int) -> bool:
        return self.find_r(v - 1) == v

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None

    def debug(self):
        def debug_info(nd_):
            return (nd_.value - 1, nd_.pivot - 1, nd_.left.value - 1 if nd_.left else -1, nd_.right.value - 1 if nd_.right else -1)

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(debug_info(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re
        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])

    def debug_list(self):
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(nd.value - 1)
            if nd.right:
                re += debug_node(nd.right)
            return re
        return debug_node(self.root)[:-1]

BT = BalancingTree(5) # 0 ～ 30 までの要素を入れられるピボット木
BT.append(3)
BT.append(20)
BT.append(5)
BT.append(10)
BT.append(13)
BT.append(8)
BT.debug()
BT.delete(20)
BT.debug()
print(BT.find_l(12)) # 10
print(BT.find_r(5)) # 8
print(BT.min) # 3
print(BT.max) # 13
print(3 in BT) # True
print(4 in BT) # False
BT.debug_list()

# 愚直チェック
from random import randrange
BT = BalancingTree(5) # 0 ～ 30 までの要素を入れられるピボット木
S = set()
for _ in range(1000):
    a = randrange(31)
    if randrange(2) == 0:
        BT.append(a)
        S.add(a)
        
    else:
        BT.delete(a)
        if a in S: S.remove(a)
    if BT.debug_list() != sorted(list(S)):
        print("NG!!")
    # print(BT.debug_list(), sorted(list(S)))
print("END")
