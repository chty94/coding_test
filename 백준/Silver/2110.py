import sys

N, C = map(int, sys.stdin.readline().split())
house = [int(sys.stdin.readline()) for _ in range(N)]
house.sort()

low, high = 1, house[-1] - house[0]

while low <= high:
    mid = (low + high) // 2

    count = 1
    cur_house = house[0]
    for h in house[1:]:
        if cur_house + mid <= h:
            count += 1
            cur_house = h

    if count >= C:
        low = mid + 1
    else:
        high = mid - 1

print(high)
