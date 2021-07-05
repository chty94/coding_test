import bisect

N = int(input().rstrip())
array = list(map(int, input().split()))

long = 0
cache = [float('inf')] * (N + 1)
cache[0] = -float('inf')

cache_ = [[] for _ in range(N + 1)]

for number in array:
    if number > cache[long]:
        long += 1
        cache[long] = number
        cache_[long] = cache_[long - 1] + [number]
    else:
        index = bisect.bisect_left(cache, number)
        cache[index] = number
        cache_[index] = cache_[index - 1] + [number]

print(long)
for i in cache_[long]:
    print(i, end=' ')
