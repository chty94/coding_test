import heapq
from collections import defaultdict

INF = float('inf')


def solution(n, start, end, roads, traps):
    graph = defaultdict(list)
    # 초기상태의 상황 입력, 3번째 인자는 방향이 맞으면 True, 방향이 반대면 False
    for a, b, cost in roads:
        graph[a].append([b, cost, True])
        graph[b].append([a, cost, False])
    # TrapToIdx는 traps의 값들을 0부터 순차적으로 넣기 위해, 궁극적으로는 비트마스킹을 이용하기 위해 변환에 필요한 딕셔너리
    TrapToIdx = dict()
    traps.sort()
    for idx, trap in enumerate(traps):
        TrapToIdx[trap] = idx
    # distances[trap_state][x] = trap_state인 상태에서 x까지 가는데 걸리는 총 cost
    distances = [[INF] * (n + 1) for _ in range(1024)]

    def dijactra(start, end):
        distances[0][start] = 0
        que = []
        heapq.heappush(que, [0, start, 0])
        while que:
            cur_dis, cur_node, cur_trap = heapq.heappop(que)
            if distances[cur_trap][cur_node] < cur_dis:
                continue
            if cur_node in traps:
                me = TrapToIdx[cur_node]
                x = True if cur_trap & (1 << me) >= 1 else False
            else:
                x = False

            '''          
            token : 초기상태 방향 판단 (True / False)
            x : cur_node에 따른 방향 (cur_node가 방향 바뀌는데 기여했으면 True 아니면 False)
            y : adj에 따른 방향 (adj가 방향 바뀌는데 기여했으면 True 아니면 False)
			token ^ (x ^ y) : 초기 상황에 대해서 방향이 몇번 틀어졌는지 계산해서 이동할 수 있는 간선인지 판단하는 식
			
            [token]	[x]		[y]		[result]
            True 	True	True -> True
            True	True	False -> False
            True	False	True -> True
            True	False	False -> False

            False	True	True -> False
            False	True	False -> True
            False	False	True -> True
            False	False	False -> False
            '''
            for adj, cost, token in graph.get(cur_node):
                if adj in traps:
                    you = TrapToIdx[adj]
                    y = True if cur_trap & (1 << you) >= 1 else False
                else:
                    y = False
                if token ^ (x ^ y):  # 이동할 수 있는 경로라면
                    if cur_dis + cost < distances[cur_trap][adj]:
                        distances[cur_trap][adj] = cur_dis + cost
                        if adj in traps:
                            next_trap = cur_trap ^ (1 << you)
                            distances[next_trap][adj] = cur_dis + cost
                            heapq.heappush(que, [cur_dis + cost, adj, next_trap])
                        else:
                            heapq.heappush(que, [distances[cur_trap][adj], adj, cur_trap])

    # 다익스트라 알고리즘 실행
    dijactra(start, end)

    # 모든 trap의 상황에 따른 end노드 까지의 값들 중 최솟값을 answer에 대입
    answer = INF
    for i in range(len(distances)):
        if distances[i][end] < answer:
            answer = distances[i][end]
    return answer


# print(solution(4, 4, 1, [[1, 2, 2], [4, 2, 3], [1, 3, 2], [4, 3, 2]], [2, 3]))
# print(solution(4, 1, 4, [[1, 2, 2], [2, 4, 3], [1, 3, 2], [3, 4, 2]], []))
print(solution(12, 1, 12,
               [[1, 2, 1], [3, 2, 1], [4, 3, 1], [5, 4, 1], [6, 5, 1], [7, 6, 1], [8, 7, 1], [9, 8, 1], [10, 9, 1],
                [11, 10, 1], [12, 11, 1]], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
