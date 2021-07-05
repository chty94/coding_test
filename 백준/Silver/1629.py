def devide_conquer(A, B, D):
    if B == 1:
        return A % D
    else:
        k = devide_conquer(A, B // 2, D)
        if B % 2 == 0:
            return (k * k) % D
        else:
            return (k * k * A) % D


A, B, D = map(int, input().split())

print(devide_conquer(A % D, B % D, D))
