import sys

N = int(sys.stdin.readline())
schedule = [0 for _ in range(367)]
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    schedule[start] += 1
    schedule[end + 1] -= 1

for i in range(1, len(schedule)):
    schedule[i] += schedule[i - 1]

width, height, result = 0, 0, 0
for s in schedule:
    if s == 0:
        result += (width * height)
        width, height = 0, 0
    else:
        width += 1
        height = max(height, s)

print(result)
