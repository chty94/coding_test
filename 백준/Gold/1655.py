
import sys
import heapq

N = int(sys.stdin.readline().rstrip())
left_heap = []  # 작은값(max_heap)
right_heap = []  # 큰값(min_heap)

heapq.heappush(left_heap, 10001)
heapq.heappush(right_heap, 10001)

for _ in range(N):
    left, right = -left_heap[0], right_heap[0]  # left는 작은 값들중 최댓값, right는 큰 값들중 최솟값
    number = int(sys.stdin.readline().rstrip())
    if len(left_heap) == len(right_heap):
        if number <= right:
            heapq.heappush(left_heap, -number)
        else:
            heapq.heappop(right_heap)
            heapq.heappush(right_heap, number)
            heapq.heappush(left_heap, -right)

    else:
        if number <= left:
            heapq.heappush(right_heap, left)
            heapq.heappop(left_heap)
            heapq.heappush(left_heap, -number)
        else:
            heapq.heappush(right_heap, number)

    print(-left_heap[0])
