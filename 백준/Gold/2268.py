import sys

N, M = map(int, input().split())
segmentTree = [0] * 4 * N
array = [0 for _ in range(N)]


def Sum(i, j, a, b, k):
    if i <= a and b <= j:
        return segmentTree[k]

    if i > b or j < a:
        return 0

    mid = (a + b) // 2
    return Sum(i, j, a, mid, 2 * k) + Sum(i, j, mid + 1, b, 2 * k + 1)


def Modify(i, diff, a, b, k):
    if i < a or b < i:
        return

    segmentTree[k] += diff

    if a != b:
        mid = (a + b) // 2
        Modify(i, diff, a, mid, 2 * k)
        Modify(i, diff, mid + 1, b, 2 * k + 1)


for _ in range(M):
    token, a, b = map(int, sys.stdin.readline().split())

    if token == 0:
        k = Sum(a - 1, b - 1, 0, len(array) - 1, 1)
        print(k)
    else:
        diff = b - array[a - 1]
        Modify(a - 1, diff, 0, len(array) - 1, 1)
        array[a - 1] = b
