from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    all_case = [dict() for _ in range((course[-1] + 1))]
    for c in course:
        for order in orders:
            for case in combinations(sorted(order), c):
                if all_case[c].get(''.join(case)):
                    all_case[c][''.join(case)] += 1
                else:
                    all_case[c][''.join(case)] = 1

    answer = []
    for c in course:
        result = sorted(all_case[c].items(), key=lambda x: [x[1], x[0]], reverse=True)

        if result:
            if result[0][1] == 1:
                continue
            max_ = result[0][1]
            for re in result:
                if max_ == re[1]:
                    answer.append(re[0])

    return sorted(answer)