# def realcheck(board, startx, starty, endx, endy):
#     for i in range(startx, endx + 1):
#         for j in range(starty, endy + 1):
#             if board[i][j] != 1:
#                 return False
#     return True
#
#
# def check(board, i, j, answer):
#     n = len(board)
#     m = len(board[0])
#
#     x, y = i + 1, j + 1
#     while x < n and y < m:
#         if board[x][y] == 0 or answer > (x - i + 1) ** 2:
#             x, y = x + 1, y + 1
#             continue
#
#         if realcheck(board, i, j, x, y):
#             answer = (x - i + 1) ** 2
#         x, y = x + 1, y + 1
#
#     return answer
#
#
# def solution(board):
#     answer = 0
#
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 1:
#                 answer = max(answer, check(board, i, j, 1))
#
#     return answer

"""
위의 코드는 정확성까지만 맞음
"""

def solution(board):
    n = len(board)
    m = len(board[0])
    answer = 0

    dp = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = board[i][0]
        answer = max(answer, board[i][0])

    for j in range(m):
        dp[0][j] = board[0][j]
        answer = max(answer, board[0][j])

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                if dp[i - 1][j - 1] > 0 and dp[i][j - 1] > 0 and dp[i - 1][j] > 0:
                    min_ = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
                    temp = int(min_ ** 0.5)
                    dp[i][j] = (temp + 1) ** 2
                    answer = max(answer, dp[i][j])
                else:
                    answer = max(1, answer)
                    dp[i][j] = board[i][j]
            else:
                dp[i][j] = board[i][j]

    return answer


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
print(solution([[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]]))

