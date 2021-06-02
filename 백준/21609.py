from collections import deque


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def find_big_block(board):
    visited = [[False for _ in range(N)] for _ in range(N)]
    count_location = []
    cl = dict()

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and board[i][j] not in [-2, -1, 0]:  # -2 : Empty, -1 : 벽, 0 : 무지개 벽돌
                block_info = [(i, j)]
                rainbow_info = []

                block = 1
                rainbow = 0

                visited[i][j] = True

                que = deque()
                que.append([i, j, board[i][j]])

                while que:
                    x, y, color = que.popleft()

                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                            if board[nx][ny] == color:
                                block_info.append((nx, ny))
                                block += 1
                                visited[nx][ny] = True
                                que.append([nx, ny, color])
                            elif board[nx][ny] == 0:
                                rainbow_info.append((nx, ny))
                                rainbow += 1
                                visited[nx][ny] = True
                                que.append([nx, ny, color])
                            else:
                                continue

                if block + rainbow < 2:
                    continue

                block_info.sort()
                cl[block_info[0]] = block_info + rainbow_info
                count_location.append([block + rainbow, rainbow, block_info[0][0], block_info[0][1]])

                for x, y in rainbow_info:
                    visited[x][y] = False

    count_location.sort(key=lambda x: [-x[0], -x[1], -x[2], -x[3]])
    if count_location:
        return [count_location[0][0], cl[(count_location[0][2], count_location[0][3])]]
    else:
        return [0]


def gravity(board):
    new_board = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[j][i] = board[i][j]

    for i in range(N):
        temp = []
        que = deque()
        for j in range(N):
            if new_board[i][j] == -2:
                que.appendleft(-2)
            elif new_board[i][j] == -1:
                que.append(-1)
                temp += list(que)
                que.clear()
            else:
                que.append(new_board[i][j])
        if que:
            temp += list(que)
        new_board[i] = temp

    for i in range(N):
        for j in range(N):
            board[j][i] = new_board[i][j]

    return board


def rotate(board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N - 1 - j][i] = board[i][j]
    return new_board


score = 0
while True:
    k = find_big_block(board)

    if k[0] == 0:
        print(score)
        break

    score += k[0] ** 2

    for x, y in k[1]:
        board[x][y] = -2

    board = gravity(board)
    board = rotate(board)
    board = gravity(board)
