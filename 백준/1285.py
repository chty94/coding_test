import copy
import sys
from itertools import combinations

N = int(sys.stdin.readline())


def total_count1(list_):
    total = 0
    for i in range(len(list_)):
        temp = list_[i]
        k = 0
        while k != N:
            if temp & (1 << k) >= 1:
                total += 1
            k += 1
    return total


def str_to_bit(bl):
    bit = []
    for i in range(len(bl)):
        bit.append(int('0b' + ''.join(bl[i]), 2))
    return bit


def bit_reverse(number):
    return number ^ ((1 << N) - 1)


def count1(number):
    count = 0
    for i in range(N):
        if (1 << i) & number >= 1:
            count += 1
    return count


bit_list = [list(map(lambda x: '0' if x == 'H' else '1', sys.stdin.readline().rstrip())) for _ in range(N)]
bit = str_to_bit(bit_list)
total = total_count1(bit)
total_list = [x for x in range(0, N)]

for count in range(1, N):
    for list_ in combinations(total_list, count):
        new_bit = copy.deepcopy(bit)
        for l in list_:
            new_bit[l] = bit_reverse(bit[l])

        new_bit2 = []
        for j in range(N - 1, -1, -1):
            value = 0
            for i in range(N):
                if new_bit[i] & (1 << j) >= 1:
                    value += 2 ** (N - 1 - i)
            new_bit2.append(value)

        real_total = 0
        for i in range(N):
            real = count1(new_bit2[i])
            if real > (N / 2):
                real_total += (N - real)
            else:
                real_total += real

        total = min(total, real_total)

print(total)
