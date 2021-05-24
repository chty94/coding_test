import sys

sys.setrecursionlimit(2000)


def solution(s):
    N = len(s)
    cache = [[None for _ in range(N)] for _ in range(N)]

    def ispalindrome(low, high):
        if cache[low][high] is not None:
            return cache[low][high]

        if low == high:
            return True
        elif low + 1 == high:
            return s[low] == s[high]

        if s[low] != s[high]:
            cache[low][high] = False
            return False
        else:
            answer = ispalindrome(low + 1, high - 1)
            cache[low][high] = answer
            return answer

    while N >= 0:
        for i in range(len(s) - N + 1):
            if ispalindrome(i, i + N - 1):
                return N
        N -= 1
