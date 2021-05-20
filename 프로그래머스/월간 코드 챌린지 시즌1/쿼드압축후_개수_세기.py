answer = [0, 0]


def dfs(arr):
    global answer

    r = len(arr)
    temp = arr[0][0]
    token = 0
    for i in range(r):
        for j in range(r):
            if arr[i][j] != temp:
                token += 1
    if token == 0:
        answer[temp] += 1
        return

    half = r // 2

    new_arr_0 = [x[:half] for x in arr[:half]]
    new_arr_1 = [x[half:] for x in arr[:half]]
    new_arr_2 = [x[:half] for x in arr[half:r]]
    new_arr_3 = [x[half:] for x in arr[half:r]]

    temp0 = new_arr_0[0][0]
    temp1 = new_arr_1[0][0]
    temp2 = new_arr_2[0][0]
    temp3 = new_arr_3[0][0]

    token0 = 0
    token1 = 0
    token2 = 0
    token3 = 0

    for i in range(half):
        for j in range(half):
            if new_arr_0[i][j] != temp0:
                token0 += 1
            if new_arr_1[i][j] != temp1:
                token1 += 1
            if new_arr_2[i][j] != temp2:
                token2 += 1
            if new_arr_3[i][j] != temp3:
                token3 += 1

    if token0 == 0:
        answer[temp0] += 1
    else:
        dfs(new_arr_0)

    if token1 == 0:
        answer[temp1] += 1
    else:
        dfs(new_arr_1)

    if token2 == 0:
        answer[temp2] += 1
    else:
        dfs(new_arr_2)

    if token3 == 0:
        answer[temp3] += 1
    else:
        dfs(new_arr_3)


def solution(arr):
    global answer
    answer = [0, 0]
    dfs(arr)
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
print(solution([[1]]))
print(solution(	[[0, 0], [0, 0]]))