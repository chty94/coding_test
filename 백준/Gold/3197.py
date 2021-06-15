import sys
from collections import deque


def melting(water_list):
    next_water_list = []
    for x, y in water_list:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 'X':
                    next_water_list.append([nx, ny])
                    board[nx][ny] = '.'
    return next_water_list


def connecting():
    que = deque()
    que.append([startx, starty])
    v = [[False] * M for _ in range(N)]
    v[startx][starty] = True

    while que:
        x, y = que.popleft()

        if x == endx and y == endy:
            return True
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not v[nx][ny]:
                v[nx][ny] = True
                if board[nx][ny] == '.':
                    que.append([nx, ny])
    return False


N, M = map(int, sys.stdin.readline().split())

check = []
board = []
water = []
visited = [[False] * M for _ in range(N)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]


for i in range(N):
    temp = sys.stdin.readline().rstrip()
    token = 0
    for j in range(M):
        if temp[j] == '.':
            water.append([i, j])
        elif temp[j] == 'L':
            token = 1
            water.append([i, j])
            check.append([i, j])

    if token == 1:
        temp = temp.replace('L', '.')

    board.append(list(temp))


startx, starty = check[0]
endx, endy = check[1]
count = 1
while True:
    water = melting(water)
    if connecting():
        print(count)
        break

    count += 1
