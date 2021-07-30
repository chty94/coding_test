import sys

N, M = map(int, input().split())
new_set = [set([i]) for i in range(N + 1)]

for _ in range(M):
    token, a, b = map(int, sys.stdin.readline().split())

    if token == 1:
        if b in new_set[a]:
            print('YES')
        else:
            print('NO')
    else:
        new_set[a].update(new_set[b])
        new_set[b].update(new_set[a])
