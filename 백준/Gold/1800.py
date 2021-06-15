import sys
from collections import defaultdict
input = sys.stdin.readline

N, P, K = map(int, input().split())
graph = defaultdict(dict)
for _ in range(P):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost
    graph[b][a] = cost

min_ = float('inf')
visited = [False for _ in range(N + 1)]
visited[1] = True
def dfs(cur_node, visited, total):
    global min_

    if cur_node == N:
        if len(total) <= K:
            print(0)
            exit(0)

        total.sort(reverse=True)
        if total[K] < min_:
            min_ = total[K]
        return

    for next in graph[cur_node]:
        if not visited[next]:
            visited[next] = True
            dfs(next, visited, total + [graph[cur_node][next]])
            visited[next] = False

dfs(1, visited, [])
if min_ == float('inf'):
    print(-1)
else:
    print(min_)
