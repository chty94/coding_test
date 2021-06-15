def findbit(numbers):
    max_ = max(numbers)
    min_ = min(numbers)
    ip = 0
    k = max_ ^ min_
    t = 7
    while True:
        if (k & (1 << t)) >= 1:
            break
        ip += (max_ & (1 << t))
        t -= 1

    bitmask = ((1 << 8) - 1) - ((1 << (t + 1)) - 1)
    return ip, bitmask

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
    temp = list(map(int, input().rstrip().split('.')))
    A.append(temp[0])
    B.append(temp[1])
    C.append(temp[2])
    D.append(temp[3])

ip_address = []
network_mask = []

if len(set(A)) == 1:
    ip_address.append(str(A[0]))
    network_mask.append(str(255))
else:
    ip, bitmask = findbit(A)
    ip_address.extend([str(ip), str(0), str(0), str(0)])
    network_mask.extend([str(bitmask), str(0), str(0), str(0)])
    print('.'.join(ip_address))
    print('.'.join(network_mask))
    exit(0)

if len(set(B)) == 1:
    ip_address.append(str(B[0]))
    network_mask.append(str(255))
else:
    ip, bitmask = findbit(B)
    ip_address.extend([str(ip), str(0), str(0)])
    network_mask.extend([str(bitmask), str(0), str(0)])
    print('.'.join(ip_address))
    print('.'.join(network_mask))
    exit(0)

if len(set(C)) == 1:
    ip_address.append(str(C[0]))
    network_mask.append(str(255))
else:
    ip, bitmask = findbit(C)
    ip_address.extend([str(ip), str(0)])
    network_mask.extend([str(bitmask), str(0)])
    print('.'.join(ip_address))
    print('.'.join(network_mask))
    exit(0)

if len(set(D)) == 1:
    ip_address.append(str(D[0]))
    network_mask.append(str(255))
else:
    ip, bitmask = findbit(D)
    ip_address.append(str(ip))
    network_mask.append(str(bitmask))

print('.'.join(ip_address))
print('.'.join(network_mask))
exit(0)
