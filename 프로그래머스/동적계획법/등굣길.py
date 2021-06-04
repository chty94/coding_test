def solution(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    puddle = {}

    for x, y in puddles:
        puddle[(y - 1, x - 1)] = True

    for x in range(1, n):
        if puddle.get((x, 0)):
            break
        else:
            board[x][0] = 1

    for y in range(1, m):
        if puddle.get((0, y)):
            break
        else:
            board[0][y] = 1

    for i in range(1, n):
        for j in range(1, m):
            if puddle.get((i, j)):
                continue
            else:
                board[i][j] = (board[i - 1][j] + board[i][j - 1]) % 1000000007

    return board[n - 1][m - 1]
