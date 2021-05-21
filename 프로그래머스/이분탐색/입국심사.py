def solution(n, times):
    times.sort()

    left = 0
    right = times[0] * n

    while left <= right:
        mid = (left + right) // 2

        temp = 0
        for time in times:
            temp += mid // time

        if n <= temp:
            right = mid - 1
        else:
            left = mid + 1

    return left