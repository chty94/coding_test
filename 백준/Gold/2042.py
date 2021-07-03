import sys
import math
input = sys.stdin.readline

N, A, B = map(int, input().split())
array = []
subTotal = 0
for _ in range(N):
    array.append(int(input().rstrip()))

segmentTree = [0] * (2 ** (math.ceil(math.log2(len(array)) + 1)) + 1)


def init(start, end, index):  # 세그먼트 트리 만들기
    if start == end:
        segmentTree[index] = array[start]
        return segmentTree[index]

    mid = (start + end) // 2
    segmentTree[index] = init(start, mid, 2 * index) + init(mid + 1, end, 2 * index + 1)
    return segmentTree[index]


def subtotal(index_left, index_right, partial_left, partial_right, index):  # 부분합
    global subTotal

    if index_right < partial_left or index_left > partial_right:
        return

    if partial_left <= index_left and index_right <= partial_right:
        subTotal += segmentTree[index]
        return

    mid = (index_left + index_right) // 2

    subtotal(index_left, mid, partial_left, partial_right, 2 * index)
    subtotal(mid + 1, index_right, partial_left, partial_right, 2 * index + 1)


def changeSubvalue(diff, segIndex, arrayIndex, start, end):  # 값 변경
    if arrayIndex < start or end < arrayIndex:
        return

    segmentTree[segIndex] += diff

    if start != end:
        mid = (start + end) // 2
        changeSubvalue(diff, 2*segIndex, arrayIndex, start, mid)
        changeSubvalue(diff, 2*segIndex + 1, arrayIndex, mid + 1, end)

init(0, len(array) - 1, 1)

T = A + B
for _ in range(T):
    token, a, b = map(int, input().split())
    if token == 2:  # 부분합 구하기
        subtotal(0, len(array) - 1, a - 1, b - 1, 1)
        print(subTotal)
        subTotal = 0
    else:  # 값 변경
        diff = b - array[a - 1]
        changeSubvalue(diff, 1, a - 1, 0, len(array) - 1)
        array[a - 1] = b
