from itertools import permutations
from collections import deque


def solution(n, weak, dist):
    answer = float('inf')
    weak = deque(weak)
    weak_size = len(weak)
    all_v = 0
    for w in weak:
        all_v |= (1 << w)

    for dist_ in permutations(dist, len(dist)):
        for _ in range(weak_size):
            v = 0
            weak.rotate(1)

            k = 0
            for w in weak:
                if k >= len(dist):
                    break
                if v & (1 << w) >= 1:
                    continue

                v |= (1 << w)
                for j in range(1, dist_[k] + 1):
                    if (w + j) % n in weak:
                        v |= (1 << (w + j) % n)
                k += 1
                if v == all_v:
                    answer = min(answer, k)
                    break

    if answer == float('inf'):
        return -1
    else:
        return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
