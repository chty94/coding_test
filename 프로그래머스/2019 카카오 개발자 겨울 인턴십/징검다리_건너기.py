def find(stones, k, mid):
    token = 0
    for stone in stones:
        if mid >= stone:
            token += 1
        else:
            token = 0

        if token >= k:
            return False
    return True


def solution(stones, k):
    answer = 0

    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2  # 징검다리를 건널 사람 추측
        token = find(stones, k, mid)
        if token:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    return answer
