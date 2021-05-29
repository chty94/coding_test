import sys
from itertools import combinations
input = sys.stdin.readline

N, K = list(map(int, input().split()))

if K < 5:
    print(0)
else:
    Alpha = 'abcdefghijklmnopqrstuvwxyz'
    Alpha_To_Number = dict()

    for idx, a in enumerate(Alpha):
        Alpha_To_Number[a] = idx

    need = 0
    need |= (1 << Alpha_To_Number['a'])
    need |= (1 << Alpha_To_Number['n'])
    need |= (1 << Alpha_To_Number['t'])
    need |= (1 << Alpha_To_Number['i'])
    need |= (1 << Alpha_To_Number['c'])

    southwords = []
    all_alpha = set()
    for _ in range(N):
        new_temp = []
        temp = list(input()[:-1])
        number = 0
        for t in temp:
            if need & (1 << Alpha_To_Number[t]) == 0:
                number |= (1 << Alpha_To_Number[t])
                all_alpha.add(t)
        southwords.append(number)

    result = []
    for t in combinations(all_alpha, K - 5):
        i = 0
        i += need
        for alpha in t:
            i |= (1 << Alpha_To_Number[alpha])

        total = 0
        for words in southwords:
            if i & words == words:
                total += 1
        result.append(total)

    if len(result) == 0:
        print(len(southwords))
    else:
        print(max(result))


