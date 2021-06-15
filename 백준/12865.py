import sys

N, max_weight = map(int, sys.stdin.readline().split())
dp_table = [[0 for _ in range(max_weight + 1)] for _ in range(N + 1)]
weight = [0]
value = [0]

for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    weight.append(w)
    value.append(v)

for i in range(1, N + 1):
    for j in range(max_weight + 1):
        if j - weight[i] >= 0:
            dp_table[i][j] = max(value[i] + dp_table[i - 1][j - weight[i]], dp_table[i - 1][j])
        else:
            dp_table[i][j] = dp_table[i - 1][j]

print(dp_table[-1][-1])
