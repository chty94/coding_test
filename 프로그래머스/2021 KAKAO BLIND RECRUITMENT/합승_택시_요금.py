def solution(n, s, a, b, fares):
    # 플로이드
    #     INF = float('inf')
    #     fluid = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    #     for i in range(1, n + 1):
    #         fluid[i][i] = 0

    #     for x, y, cost in fares:
    #         fluid[x][y] = cost
    #         fluid[y][x] = cost

    #     for k in range(1, n + 1):
    #         for i in range(1, n + 1):
    #             for j in range(1, n + 1):
    #                 if fluid[i][k] + fluid[k][j] < fluid[i][j]:
    #                     fluid[i][j] = fluid[i][k] + fluid[k][j]

    #     min_ = float('inf')
    #     for k in range(1, n + 1):
    #         temp = fluid[s][k] + fluid[k][a] + fluid[k][b]
    #         if temp < min_:
    #             min_ = temp

    #     return min_

    # 다익스트라
    import heapq
    from collections import defaultdict

    def dijacstra(n, graph, start, end):
        distances = [float('inf') for _ in range(n + 1)]
        que = []
        distances[start] = 0
        heapq.heappush(que, [0, start])

        while que:
            cur_cost, cur_location = heapq.heappop(que)
            if distances[cur_location] < cur_cost:
                continue
            for adjacent in graph[cur_location]:
                if distances[cur_location] + graph[cur_location][adjacent] < distances[adjacent]:
                    distances[adjacent] = distances[cur_location] + graph[cur_location][adjacent]
                    heapq.heappush(que, [distances[adjacent], adjacent])

        return distances[end]

    graph = defaultdict(dict)
    for x, y, cost in fares:
        graph[x][y] = cost
        graph[y][x] = cost

    total = float('inf')
    for k in range(1, n + 1):
        s_k = dijacstra(n, graph, s, k)
        k_a = dijacstra(n, graph, k, a)
        k_b = dijacstra(n, graph, k, b)
        if s_k + k_a + k_b < total:
            total = s_k + k_a + k_b
    return total

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(	6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
