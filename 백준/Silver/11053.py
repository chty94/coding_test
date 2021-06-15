# import sys
#
# input = sys.stdin.readline
# sys.setrecursionlimit(1000000)
#
# N = int(input())
# array = list(map(int, input().split()))
#
# cache = [0 for _ in range(N)]
# long = 0
#
#
# def bisect(array, number):
#     lo, hi = 0, len(array) - 1
#
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if number == array[mid]:
#             return mid
#         elif number > array[mid]:
#             lo = mid + 1
#         else:
#             hi = mid - 1
#     return lo
#
#
# cache[0] = array[0]
# for number in array[1:]:
#     if number > cache[long]:
#         long += 1
#         cache[long] = number
#     else:
#         index = bisect(cache[:long + 1], number)
#         cache[index] = number
#
# print(long + 1)
#
#
import sys

input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))

def lis(arr):
    if not arr:
        return 0

    # C[i] means smallest last number of lis subsequences whose length are i
    INF = float('inf')
    C = [INF] * (len(arr)+1)
    C[0] = -INF
    C[1] = arr[0]
    tmp_longest = 1

    # Find i that matches C[i-1] < n <= C[i]
    def search(lo, hi, n):
        if lo == hi:
            return lo
        elif lo + 1 == hi:
            return lo if C[lo] >= n else hi

        mid = (lo + hi) // 2
        if C[mid] == n:
            return mid
        elif C[mid] < n:
            return search(mid+1, hi, n)
        else:
            return search(lo, mid, n)


    for n in arr:
        if C[tmp_longest] < n:
            tmp_longest += 1
            C[tmp_longest] = n
        else:
            next_loc = search(0, tmp_longest, n)
            C[next_loc] = n

    return tmp_longest

print(lis(array))
