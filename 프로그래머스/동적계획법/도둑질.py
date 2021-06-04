def solution(money):
    Sn = [0] * len(money)

    # 첫번째 집 O
    Sn[0] = money[0]
    Sn[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):
        Sn[i] = max(Sn[i - 1], Sn[i - 2] + money[i])

    temp = Sn[len(money) - 2]

    # 첫번째 집 X
    Sn[0] = 0
    Sn[1] = money[1]

    for i in range(2, len(money)):
        Sn[i] = max(Sn[i - 1], Sn[i - 2] + money[i])

    return max(temp, Sn[len(money) - 1])
