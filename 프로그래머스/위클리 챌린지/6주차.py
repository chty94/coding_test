def solution(weights, head2head):
    answer = []

    for idx, WinNullLose in enumerate(head2head):
        me_weight = weights[idx]
        WNL = list(WinNullLose)
        win = 0
        lose = 0
        count = 0
        for weight, result in zip(weights, WNL):
            if result == "N":
                continue
            elif result == "W":
                win += 1
                if weight > me_weight:
                    count += 1
            else:  # result == "L":
                lose += 1
        if (win + lose) == 0:
            answer.append([0, 0, me_weight, idx + 1])
        else:
            answer.append([win / (win + lose), count, me_weight, idx + 1])

    result = []
    answer.sort(key=lambda x: [-x[0], -x[1], -x[2], x[3]])
    for _, _, _, k in answer:
        result.append(k)
    return result