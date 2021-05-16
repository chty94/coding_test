import sys
sys.setrecursionlimit(10**6)


def solution(nodeinfo):
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    class Tree:
        def __init__(self, data):
            self.head = Node(data)

        def add(self, data):
            cur = self.head
            while cur:
                _, x, y = cur.data
                if data[1] < x:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        return
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        return

        def postorder(self):
            postorder_list = []

            def _postorder(root):
                if root.left:
                    _postorder(root.left)
                if root.right:
                    _postorder(root.right)
                postorder_list.append(root.data[0])

            _postorder(self.head)
            return postorder_list

        def preorder(self):
            preorder_list = []

            def _preorder(root):
                preorder_list.append(root.data[0])
                if root.left:
                    _preorder(root.left)
                if root.right:
                    _preorder(root.right)

            _preorder(self.head)
            return preorder_list

    new_nodeinfo = []
    for idx, xy in enumerate(nodeinfo):
        new_nodeinfo.append([idx + 1, xy[0], xy[1]])

    new_nodeinfo.sort(key=lambda x: [-x[2], x[1], x[0]])
    binary = Tree(new_nodeinfo[0])

    for xy in new_nodeinfo[1:]:
        binary.add(xy)

    preorder = binary.preorder()
    postorder = binary.postorder()

    answer = [preorder, postorder]
    return answer
