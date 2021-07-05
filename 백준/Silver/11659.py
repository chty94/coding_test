import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
Sn = [0] * (len(array) + 1)
for i in range(len(array)):
    Sn[i + 1] = Sn[i] + array[i]

for _ in range(M):
    a, b = map(int, input().split())
    print(Sn[b] - Sn[a - 1])
