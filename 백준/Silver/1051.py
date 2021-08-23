N, M = map(int, input().split())
array = []
for _ in range(N):
    array.append(list(input().rstrip()))

def check(array, i, j, N, M):
    key = array[i][j]

    result = 0
    max_ = min(N - i, M - j)
    for k in range(1, max_):
        if key == array[i + k][j] == array[i][j + k] == array[i + k][j + k]:
            result = max(result, ((k + 1) ** 2))
    return result

answer = 1
for i in range(N - 1):
    for j in range(M - 1):
        answer = max(answer, check(array, i, j, N, M))
print(answer)
