answer = 0

def solution(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    def N_Queen(board, i, col):
        global answer
        if i == N:
            answer += 1
            return

        for j in range(len(board)):
            if col & (1 << N - 1 - j) >= 1:
                continue
            k = 1
            for m in range(i - 1, -1, -1):
                if j + k < N and board[m][j + k] == 1:
                    break
                if j - k >= 0 and board[m][j - k] == 1:
                    break
                k += 1
            else:
                board[i][j] = 1
                N_Queen(board, i + 1, col | (1 << N - 1 - j))
                board[i][j] = 0

    N_Queen(board, 0, 0)
    return answer


print(solution(4))
