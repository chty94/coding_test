import sys


def maxSquare(histogram, i, j):
    if i == j:
        return histogram[i]
    else:
        left_mid = (i + j) // 2
        right_mid = left_mid + 1

        height = min(histogram[left_mid], histogram[right_mid])
        length = 2
        tmp = height * length

        while True:
            if (left_mid == i or histogram[left_mid] == 0) and (right_mid == j or histogram[right_mid] == 0):
                break

            elif left_mid == i or histogram[left_mid] == 0:
                right_mid += 1
                if histogram[right_mid] < height:
                    height = histogram[right_mid]

            elif right_mid == j or histogram[right_mid] == 0:
                left_mid -= 1
                if histogram[left_mid] < height:
                    height = histogram[left_mid]

            else:
                if histogram[left_mid - 1] < histogram[right_mid + 1]:
                    if histogram[right_mid + 1] < height:
                        height = histogram[right_mid + 1]
                    right_mid += 1
                else:
                    if histogram[left_mid - 1] < height:
                        height = histogram[left_mid - 1]
                    left_mid -= 1

            length += 1
            tmp = max(tmp, length * height)

        return max(maxSquare(histogram, i, (i + j) // 2), maxSquare(histogram, ((i + j) // 2) + 1, j), tmp)


while True:
    temp = sys.stdin.readline().split()
    if temp[0] == '0':
        break

    N = int(temp[0])
    histogram = list(map(int, temp[1:]))
    print(maxSquare(histogram, 0, N - 1))
