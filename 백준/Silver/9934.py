def devide_conquer(arr, height):
    N = len(arr)
    if N == 1:
        tree[height].append(arr[0])
        return

    mid = N // 2
    tree[height].append(arr[mid])
    devide_conquer(arr[:mid], height + 1)
    devide_conquer(arr[mid + 1:], height + 1)


K = int(input())
arr = list(map(int, input().split()))
tree = {i: [] for i in range(1, K + 1)}
devide_conquer(arr, 1)
for key in tree.keys():
    print(*tree[key])
