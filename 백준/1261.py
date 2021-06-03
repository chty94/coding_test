import sys
from collections import deque


M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

que = deque()
que.append([0, 0, 0])
dxy = [[0, 1], [1, 0]]
total = float('inf')

while que:
    x, y, wall = que.popleft()
    if x == N - 1 and y == M - 1:
        total = min(total, wall)
        continue

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1:
                que.append([nx, ny, wall + 1])
            else:
                que.append([nx, ny, wall])

print(total)



