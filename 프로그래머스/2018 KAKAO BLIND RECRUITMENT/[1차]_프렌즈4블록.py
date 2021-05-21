# def check(m, n, board):
#     candidate = set()
#     for i in range(m - 1):
#         for j in range(n - 1):
#             if board[i][j] == 'X':
#                 continue
#             if board[i][j] == board[i + 1][j] and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j + 1]:
#                 candidate.add((i, j))
#                 candidate.add((i + 1, j))
#                 candidate.add((i, j + 1))
#                 candidate.add((i + 1, j + 1))
#
#     return candidate
#
#
# def down(m, n, board):
#     for j in range(n):
#         for i in range(m - 1, -1, -1):
#             if board[i][j] == 'X':
#                 ii, jj = i, j
#                 while board[ii][jj] == 'X':
#                     ii -= 1
#                     if ii == -1:
#                         break
#                 if ii == -1:
#                     break
#                 board[i][j], board[ii][jj] = board[ii][jj], board[i][j]
#     return board
#
#
# def solution(m, n, board):
#     answer = 0
#     board = [list(board[x]) for x in range(m)]
#
#     while True:
#         candidate = check(m, n, board)
#         if len(candidate) == 0:
#             return answer
#
#         for x, y in candidate:
#             board[x][y] = 'X'
#             answer += 1
#
#         board = down(m, n, board)
#
#     return answer

def solution(m, n, board):
    answer = 0
    new_board = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            new_board[i][j] = board[j][i]

    while True:
        candidate = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if new_board[i][j] == new_board[i + 1][j] == new_board[i][j + 1] == new_board[i + 1][j + 1] != 'X':
                    candidate.add((i, j))
                    candidate.add((i + 1, j))
                    candidate.add((i, j + 1))
                    candidate.add((i + 1, j + 1))

        if len(candidate) == 0:
            return answer

        for x, y in candidate:
            new_board[x][y] = 'X'
            answer += 1

        for idx, values in enumerate(new_board):
            countX = new_board[idx].count('X')
            if countX != 0:
                new_board[idx] = ['X' for _ in range(countX)] + [x for x in values if x != 'X']

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
