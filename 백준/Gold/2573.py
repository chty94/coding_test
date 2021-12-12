import sys
from collections import defaultdict
from collections import deque


def check():
    visited = [[False] * M for _ in range(N)]
    count = 0
    for x in range(1, N - 1):
        for y in range(1, M - 1):
            if sea[x][y] != 0 and not visited[x][y]:
                count += 1
                que = deque()
                que.append((x, y))
                visited[x][y] = True

                while que:
                    n, m = que.popleft()
                    for dx, dy in dxy:
                        nx, ny = n + dx, m + dy
                        if not visited[nx][ny] and sea[nx][ny] != 0:
                            visited[nx][ny] = True
                            que.append((nx, ny))
    return count


def melt():
    temp = defaultdict(int)
    for x in range(1, N - 1):
        for y in range(1, M - 1):
            if sea[x][y] != 0:
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if sea[nx][ny] == 0:
                        temp[(x, y)] += 1
    return temp


N, M = map(int, sys.stdin.readline().split())
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
sea = []

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    sea.append(temp)

year = 0
while True:
    count = check()
    if count >= 2:
        break
    temp = melt()
    if not temp:
        year = 0
        break
    else:
        for x, y in temp:
            sea[x][y] -= min(temp[(x, y)], sea[x][y])
        year += 1

print(year)
