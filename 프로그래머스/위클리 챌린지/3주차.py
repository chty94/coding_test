dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def normalization(shape):
    x = sorted(shape, key=lambda x: [x[0], x[1]])
    y = sorted(shape, key=lambda x: [x[1], x[0]])

    min_x, min_y = x[0][0], y[0][1]
    normalization_shape = []

    for x, y in shape:
        normalization_shape.append([x - min_x, y - min_y])
    normalization_shape.sort()
    return normalization_shape


def dfs(table, i, j, value):
    result = []
    stack = [[i, j]]
    N = len(table)
    table[i][j] = value ^ 1
    while stack:
        x, y = stack.pop()
        result.append([x, y])

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and table[nx][ny] == value:
                stack.append([nx, ny])
                table[nx][ny] = value ^ 1
    result = normalization(result)
    return result


def rotate(shapes, N):
    new_shapes = []
    for shape in shapes:
        new_shape = []
        for x, y in shape:
            new_shape.append([y, N - 1 - x])
        new_shape = normalization(new_shape)
        new_shapes.append(new_shape)
    return new_shapes


def solution(game_board, table):
    answer = 0

    N = len(table)
    shapes = []
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                shapes.append(dfs(table, i, j, 1))

    boards = []
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0:
                boards.append(dfs(game_board, i, j, 0))

    shapes0 = shapes
    shapes1 = rotate(shapes0, N)
    shapes2 = rotate(shapes1, N)
    shapes3 = rotate(shapes2, N)

    total_shapes = []
    for i in range(len(shapes)):
        total_shapes.append([shapes0[i], shapes1[i], shapes2[i], shapes3[i]])

    board_token = [False] * len(boards)
    token = [False] * len(total_shapes)
    for i, board in enumerate(boards):
        for idx, shapes in enumerate(total_shapes):
            if not token[idx] and not board_token[i]:
                for shape in shapes:
                    if board == shape:
                        token[idx] = True
                        board_token[i] = True
                        break
                if token[idx]:
                    answer += len(board)
    return answer
