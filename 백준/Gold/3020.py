import sys
import bisect

N, H = map(int, sys.stdin.readline().split())
obstacle = []
for _ in range(N):
    obstacle.append(int(sys.stdin.readline()))

bottom = [o for o in obstacle[::2]]
top = [o for o in obstacle[1::2]]
length = len(obstacle) // 2
top.sort()
bottom.sort()

ttop = [0] * (H + 1)
bbot = [0] * (H + 1)
for k in range(1, H + 1):
    topLeftIndex = bisect.bisect_left(top, H + 1 - k)
    topRightIndex = bisect.bisect_right(top, H + 1 - k)
    bottomLeftIndex = bisect.bisect_left(bottom, k)
    bottomRightIndex = bisect.bisect_right(bottom, k)

    countTopK = topRightIndex - topLeftIndex
    countBottomK = bottomRightIndex - bottomLeftIndex

    ttop[k] += countTopK
    bbot[k] += countBottomK

for i in range(len(ttop) - 2, 0, -1):
    bbot[i] += bbot[i + 1]
for i in range(1, len(ttop)):
    ttop[i] += ttop[i - 1]

count = 0
min_ = float('inf')
for b, t in zip(bbot[1:], ttop[1:]):
    if b + t < min_:
        min_ = b + t
        count = 1
    elif b + t == min_:
        count += 1
print(min_, count)
