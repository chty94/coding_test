array = [i for i in range(1, 11)]
tree = [0] * 4 * len(array)


def init(start, end, index):
    if start == end:
        tree[index] = array[start]
        return tree[index]
    mid = (start+end)//2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return tree[index]

init(0, 9, 1)
print(tree)
