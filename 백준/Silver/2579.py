import sys

N = int(sys.stdin.readline().rstrip())
An = [0]

for _ in range(N):
    An.append(int(sys.stdin.readline().rstrip()))

if N == 1:
    print(An[1])
    exit(0)
elif N == 2:
    print(An[1] + An[2])
    exit(0)
else:
    Sn = [0, An[1], An[1] + An[2]]
    for n in range(3, N + 1):
        Sn.append(max(Sn[n - 3] + An[n - 1] + An[n], Sn[n - 2] + An[n]))
    print(Sn[N])
