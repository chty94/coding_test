import sys
import heapq


M, N = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

que = []
heapq.heappush(que, [0, 0, 0])
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
distances = [[float('inf')] * M for _ in range(N)]
distances[0][0] = 0

while que:
    x, y, dist = heapq.heappop(que)
    if x == N - 1 and y == M - 1:
        print(dist)
        exit(0)

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            new_distance = dist + board[nx][ny]
            if new_distance < distances[nx][ny]:
                distances[nx][ny] = new_distance
                heapq.heappush(que, [nx, ny, new_distance])
