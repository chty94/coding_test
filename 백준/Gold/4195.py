import sys
sys.setrecursionlimit(100000)

def find(friend):
    if friends[friend] == friend:
        return friend
    else:
        parent = find(friends[friend])
        friends[friend] = parent
        return parent


def union(fr1, fr2):
    parent1 = find(fr1)
    parent2 = find(fr2)

    if parent1 != parent2:
        friends[parent2] = parent1
        friends[fr2] = parent1
        friends_number[parent1] += friends_number[parent2]
    print(friends_number[parent1])

T = int(sys.stdin.readline())
for _ in range(T):
    friends = dict()
    friends_number = dict()
    N = int(sys.stdin.readline())

    for _ in range(N):
        friend1, friend2 = sys.stdin.readline().split()

        if friend1 not in friends.keys():
            friends[friend1] = friend1
            friends_number[friend1] = 1
        if friend2 not in friends.keys():
            friends[friend2] = friend2
            friends_number[friend2] = 1
        union(friend1, friend2)
