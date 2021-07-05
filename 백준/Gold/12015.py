import bisect

N = int(input().rstrip())
array = list(map(int, input().split()))

long = 0
cache = [float('inf')] * (N + 1)
cache[0] = -float('inf')

for number in array:
    if number > cache[long]:
        long += 1
        cache[long] = number
    else:
        index = bisect.bisect_left(cache, number)
    if cache[index] != number:
        cache[index] = number

print(long)

