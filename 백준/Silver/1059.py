import bisect

L = int(input())
S = list(map(int, input().split()))
N = int(input())

S.sort()
l = bisect.bisect_left(S, N)
r = bisect.bisect_right(S, N)

left, right = S[l], S[r]
if left == N:
    print(0)
else:
    left = S[l - 1]
    if N < S[0]:
        left = 0

    countL = N - left - 1
    countR = right - 1 - N
    result = countL + countR + countL * countR
    print(result)
