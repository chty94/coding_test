def solution(n):
    Sn = [0] * (n + 1)
    Sn[1] = 1
    Sn[2] = 2

    if n <= 2:
        return Sn[n]
    else:
        for i in range(3, n + 1):
            Sn[i] = (Sn[i - 1] + Sn[i - 2]) % 1000000007

    return Sn[n]