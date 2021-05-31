import sys
N = int(sys.stdin.readline())
list_ = [list(map(lambda x: '0' if x == 'H' else '1', sys.stdin.readline().rstrip())) for _ in range(N)]


def column(bit, n):
    check = 0
    for i in range(n, N*(N - 1) + 1, N):
        check = check | (1 << i)
    return bit ^ check


def row(bit, n):
    if n == 0:
        check = (1 << N) - 1
    else:
        s, e = (n + 1) * N, n * N
        check = ((1 << s) - 1) - ((1 << e) - 1)
    return bit ^ check


def COUNT(bit):
    count = 0
    for i in range(N * N):
        check = (1 << i)
        if bit & check >= 1:
            count += 1
    return count


bit = ''
for i in range(len(list_)):
    bit = ''.join(list_[i][::-1]) + bit
bit = '0b' + bit
bit = int(bit, 2)
total = []

def dfs(bit, n, count):
    if count >= 2 * N:
        total.append(COUNT(bit))
        return

    if n < N:
        dfs(bit, n + 1, count + 1)
        new_bit = row(bit, n)
        dfs(new_bit, n + 1, count + 1)

    else:
        dfs(bit, n + 1, count + 1)
        new_bit = column(bit, n - N)
        dfs(new_bit, n + 1, count + 1)

dfs(bit, 0, 0)
print(min(total)


