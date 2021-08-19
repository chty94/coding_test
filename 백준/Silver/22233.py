# 가희와 키워드
import sys

N, M = map(int, sys.stdin.readline().split())
keyword = {}
total = N

for _ in range(N):
    keyword[sys.stdin.readline().rstrip()] = True

for _ in range(M):
    temp = sys.stdin.readline().rstrip().split(',')
    for t in temp:
        if keyword.get(t):
            total -= 1
            del keyword[t]
    print(total)
