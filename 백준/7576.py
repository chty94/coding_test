import sys
from collections import deque
input = sys.stdin.readline


M, N = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
que = deque()
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            que.append([i, j, 1])

while que:
    x, y, count = que.popleft()

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0:
                board[nx][ny] = count + 1
                que.append([nx, ny, count + 1])

result = -1
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            print(-1)
            exit(0)
        else:
            result = max(result, board[i][j])
print(result - 1)
