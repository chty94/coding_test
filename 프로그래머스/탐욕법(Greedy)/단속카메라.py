def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[1])
    check = []
    check.append(routes[0][1])
    answer += 1

    for x, y in routes:
        token = False
        for k in check:
            if x <= k <= y:
                token = True
                break
        if token:
            continue
        else:
            check.append(y)
            answer += 1

    return answer
