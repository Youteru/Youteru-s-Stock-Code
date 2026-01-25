from functools import cmp_to_key


def arg_sort(p0, p1):
    x0, y0 = p0
    x1, y1 = p1
    if x0 * y1 == x1 * y0:
        return 0
    return 1 if x0 * y1 < x1 * y0 else -1


N = int(input())
lst = []
for _ in range(N):
    x, y = map(int, input().split())
    lst.append((x, y))
lst.sort(key=cmp_to_key(arg_sort))
