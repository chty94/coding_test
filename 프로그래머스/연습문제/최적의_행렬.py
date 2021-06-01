def solution(matrix_sizes):
    answer = 0
    d = [matrix_sizes[0][0], matrix_sizes[0][1]]
    INF = float('inf')
    cache = [[INF for _ in range(len(matrix_sizes))] for _ in range(len(matrix_sizes))]
    for i in range(len(matrix_sizes)):
        cache[i][i] = 0
    for x, y in matrix_sizes[1:]:
        d.append(y)

    def matrix(i, j):
        if cache[i][j] != INF:
            return cache[i][j]

        if i + 1 == j:
            temp = d[i] * d[i + 1] * d[i + 2]
            cache[i][j] = temp
            return cache[i][j]

        min_ = []
        for k in range(i, j):
            min_.append(matrix(i, k) + matrix(k + 1, j) + (d[i] * d[k + 1] * d[j + 1]))
        cache[i][j] = min(min_)
        return cache[i][j]

    return matrix(0, len(matrix_sizes) - 1)

print(solution([[5,3],[3,10],[10,6]]))
