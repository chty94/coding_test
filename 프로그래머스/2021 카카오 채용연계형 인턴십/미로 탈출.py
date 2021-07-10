"""
1. 트랩으로 이동하면 트랩에 연결된 간선들의 방향이 바뀐다.
    -> 초기상태 그래프에서 하나의 정점(V)에 대해서 출발하는 경우는 1, 도착하는 경우는 0으로 V와 관련 모든 간선(E)을 담는다.
        ex) graph[v] = [[v', cost, 1], [v'', cost', 0] ...]
        -> v에서 v'으로 가는데 cost 비용이 듦
        -> v''에서 v로 가는데 cost 비용이 듦
        ...

2. 다익스트라는 최소 이동 거리를 찾는 알고리즘인데 정점에 대해 재방문 하는 경우는 일어나지 않는다.
    -> 트랩을 밟을 경우에 한해 그 위치에서 다시 다익스트라 알고리즘을 실행한다.
    -> 이는 가능한 트랩 수는 10개이기에 총 2^10 = 1024개의 다익스트라 알고리즘을 사용 할 가능성을 의미함.
"""

import heapq
from collections import defaultdict
import sys

sys.setrecursionlimit(100000)


def solution(n, start, end, roads, traps):
    graph = defaultdict(list)
    for x, y, cost in roads:  # 어떤 트랩도 밟지 않은 상태에서의 경로
        # x노드에서 y노드로 갈때 cost의 비용이 든다.
        graph[x].append([y, cost, 1])
        graph[y].append([x, cost, 0])

    TrapToindex = {}
    indexToTrap = {}
    traps.sort()

    for idx, trap in enumerate(traps):
        TrapToindex[trap] = idx + 1
        indexToTrap[idx + 1] = trap

    visited = [[False] * (1 << len(traps) + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        visited[i][0] = True

    def dijactra(start, end, trap_list):  # now_trap(비트연산)인 상태에서 start에서 end까지의 가는 다익스트라 알고리즘
        k = 0
        now_trap = 0
        for t in trap_list:
            now_trap ^= (1 << t)
            trap_idx = TrapToindex[t]
            k ^= (1 << trap_idx)

        if k != 0 and visited[start][k]:
            return 0
        visited[start][k] = True

        INF = float('inf')
        distances = [INF for _ in range(n + 1)]
        distances[start] = 0

        que = []
        heapq.heappush(que, [0, start])
        while que:
            cur_distance, cur_node = heapq.heappop(que)

            if distances[cur_node] < cur_distance:
                continue

            a = 1 if now_trap & (1 << cur_node) >= 1 else 0
            for next, cost, token in graph.get(cur_node):
                b = 1 if now_trap & (1 << next) >= 1 else 0
                if token ^ (a ^ b) >= 1:
                    if next in traps:
                        temp = dijactra(next, end, trap_list + [next])
                        if temp == 0:
                            continue
                        if distances[cur_node] + cost + temp < distances[end]:
                            distances[end] = distances[cur_node] + temp + cost
                    else:
                        if distances[cur_node] + cost < distances[next]:
                            distances[next] = distances[cur_node] + cost
                            if next != end:
                                heapq.heappush(que, [distances[next], next])

        if distances[end] == INF:
            return 0
        else:
            return distances[end]

    return dijactra(start, end, [])