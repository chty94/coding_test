import sys

N, M = map(int, input().split())
new_set = {i: i for i in range(N + 1)}


def find(x):
    if new_set[x] == x:
        return x
    return find(new_set[x])

for _ in range(M):
    token, a, b = map(int, sys.stdin.readline().split())
    pa, pb = find(a), find(b)

    if token == 1:
        if pa == pb:
            print('YES')
        else:
            print('NO')
    else:
        if pa != pb:
            new_set[pb] = pa
            new_set[b] = pa
