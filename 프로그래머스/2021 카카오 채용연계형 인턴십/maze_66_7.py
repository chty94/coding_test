from collections import defaultdict
import heapq
import sys
sys.setrecursionlimit(1000000)

def solution(n, start, end, roads, traps):
    TrapToIdx = dict()
    IdxToTrap = dict()
    graph = defaultdict(list)
    traps.sort()
    visited = [False] * (1 << len(traps))
    # visited[a][b][trap] = trap인 상황에서 a에서 b로 가는 경우를 방문 했는지 여부

    INF = float('inf')
    distances = [[INF] * (n + 1) for _ in range(1 << len(traps))]

    for idx, trap in enumerate(traps):
        TrapToIdx[trap] = idx
        IdxToTrap[idx] = trap

    for x, y, cost in roads:
        graph[x].append([y, cost, 0])
        graph[y].append([x, cost, 1])


    def dijactra(start, end, now_trap):
        if visited[now_trap]:
            return distances[now_trap][start]
        visited[now_trap] = True

        distances[now_trap][start] = 0
        que = []
        heapq.heappush(que, [0, start])

        while que:
            cur_distance, cur_node = heapq.heappop(que)

            if distances[now_trap][cur_node] < cur_distance:
                continue

            if cur_node in traps:
                t1 = TrapToIdx[cur_node]
                s = 1 if now_trap & (1 << t1) >= 1 else 0
            else:
                s = 0

            for next, cost, token in graph.get(cur_node):
                if next in traps:
                    t2 = TrapToIdx[next]
                    e = 1 if now_trap & (1 << t2) >= 1 else 0
                else:
                    e = 0

                if token ^ (s ^ e) == 0:
                    if next in traps:
                        tti = TrapToIdx[next]
                        temp = dijactra(next, end, now_trap ^ (1 << tti))
                        distance = cur_distance + cost
                        if distance < distances[now_trap][next]:
                            distances[now_trap][next] = distance

                        if cur_distance + cost + temp < distances[now_trap][end]:
                            distances[now_trap][end] = cur_distance + cost + temp
                    else:
                        distance = cur_distance + cost
                        if distance < distances[now_trap][next]:
                            distances[now_trap][next] = distance
                            heapq.heappush(que, [distance, next])

        return distances[now_trap][end]

    answer = dijactra(start, end, 0)
    return answer

print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
