import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
array = list(map(int, input().split()))

cache = [float('inf') for _ in range(N + 1)]
cache[0] = -float('inf')
long = 1


def bisect(array, number):
    lo, hi = 0, len(array) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if number == array[mid]:
            return mid
        elif number > array[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo


def increasing(array):
    global long

    cache[1] = array[0]
    for number in array[1:]:
        if number > cache[long]:
            long += 1
            cache[long] = number
        else:
            index = bisect(cache[1:long + 1], number)
            cache[index + 1] = number


increasing(array)
print(long)
