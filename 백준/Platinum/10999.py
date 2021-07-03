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


def sumDiff(diff, segIndex, segLeft, segRight, arrayLeft, arrayRight):  # 값 변경
    if segRight < arrayLeft or segLeft > arrayRight:
        return

    if segLeft <= arrayLeft and arrayRight <= segRight:
        segmentTree[segIndex] += (diff * (arrayRight - arrayLeft + 1))
    elif arrayLeft <= segLeft and segRight <= arrayRight:
        segmentTree[segIndex] += (diff * (segRight - segLeft + 1))
    else:
        if arrayLeft < segLeft:
            segmentTree[segIndex] += (diff * (arrayRight - segLeft + 1))
        else:
            segmentTree[segIndex] += (diff * (segRight - arrayLeft + 1))

    if segLeft != segRight:
        mid = (segLeft + segRight) // 2
        sumDiff(diff, 2 * segIndex, segLeft, mid, arrayLeft, arrayRight)
        sumDiff(diff, 2 * segIndex + 1, mid + 1, segRight, arrayLeft, arrayRight)


init(0, len(array) - 1, 1)
T = A + B
for _ in range(T):
    token = list(map(int, input().split()))
    if token[0] == 2:  # 부분합 구하기
        a, b = token[1], token[2]
        subtotal(0, len(array) - 1, a - 1, b - 1, 1)
        print(subTotal)
        subTotal = 0
    else:  # 값 변경
        a, b, diff = token[1], token[2], token[3]
        sumDiff(diff, 1, 0, len(array) - 1, a - 1, b - 1)
