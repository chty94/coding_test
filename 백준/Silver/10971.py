import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().rstrip().split())) for _ in range(N)]

def TSP(W):
    cache = [[None] * (1 << N) for _ in range(N)]
    all_visited = (1 << N) - 1
    INF = float('inf')

    def find_path(last, visited):
        if visited == all_visited:
            return W[last][0] or INF

        if cache[last][visited] is not None:
            return cache[last][visited]

        tmp = INF
        for city in range(N):
            if visited & (1 << city) == 0 and W[last][city] != 0:
                tmp = min(tmp, find_path(city, visited | (1 << city)) + W[last][city])
                cache[last][visited] = tmp
        return tmp

    return find_path(0, 1 << 0)

print(TSP(W))
