import copy

def rotate(key):
    n = len(key)

    new_key = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_key[i][j] += key[j][n - 1 - i]

    return new_key


def compare(array, key, rot, r, c, lock):
    n = len(key)

    if rot == 0:
        pass
    elif rot == 1:
        key = rotate(key)
    elif rot == 2:
        key = rotate(key)
        key = rotate(key)
    else:
        key = rotate(key)
        key = rotate(key)
        key = rotate(key)

    for i in range(n):
        for j in range(n):
            array[r + i][c + j] += key[i][j]

    for i in range(lock):
        for j in range(lock):
            if array[lock - 1 + i][lock - 1 + j] != 1:
                return False
    return True



def solution(key, lock):
    array = [[0 for _ in range(58)] for _ in range(58)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            array[i + len(lock) - 1][j + len(lock) - 1] = lock[i][j]

    for r in range(len(lock) + len(lock) - 1):
        for c in range(len(lock) + len(lock) - 1):
            for rot in range(4):
                temp = copy.deepcopy(array)
                if compare(temp, key, rot, r, c, len(lock)):
                    return True
    return False



print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
