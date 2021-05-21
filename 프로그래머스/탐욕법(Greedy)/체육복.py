def solution(n, lost, reserve):
    answer = 0
    init = [1 for _ in range(n + 2)]
    lost.sort()
    reserve.sort()

    for l in lost:
        init[l] -= 1

    for r in reserve:
        init[r] += 1

    print(init)

    for r in reserve:
        if init[r] == 1:
            continue
        else:
            if init[r - 1] == 0 and init[r + 1] == 0:
                init[r] -= 1
                init[r - 1] += 1
            elif init[r - 1] == 0:
                init[r] -= 1
                init[r - 1] += 1
            elif init[r + 1] == 0:
                init[r] -= 1
                init[r + 1] += 1
    return n - init.count(0)