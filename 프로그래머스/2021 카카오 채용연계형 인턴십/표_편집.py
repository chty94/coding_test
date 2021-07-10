def solution(n, k, cmd):
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    class Linkedlist:
        def __init__(self):
            self.head = Node(-1)
            self.cur_address = self.head

        def insert(self, count, k):
            cur = self.head
            for data in range(count):
                cur.next = Node(data)
                cur.next.prev = cur
                cur = cur.next

                if data == k:
                    self.cur_address = cur

            cur.next = Node(-1)
            cur.next.prev = cur

        def down(self, x):
            cur = self.cur_address
            while x > 0:
                cur = cur.next
                x -= 1
            self.cur_address = cur

        def up(self, x):
            cur = self.cur_address
            while x > 0:
                cur = cur.prev
                x -= 1
            self.cur_address = cur

        def c(self):
            cur = self.cur_address
            if cur.next.data == -1 and cur.prev.data != -1:
                self.cur_address = cur.prev
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
            else:
                self.cur_address = cur.next
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
            return cur

        def z(self, address):
            address.prev.next = address
            address.next.prev = address

        def result(self, total):
            result = ['X'] * total
            cur = self.head.next
            while cur.data != -1:
                result[cur.data] = 'O'
                cur = cur.next

            return ''.join(result)

    address_stack = []
    Link = Linkedlist()
    Link.insert(n, k)

    for k in cmd:
        k = k.split()
        if k[0] == 'D':
            number = int(k[1])
            Link.down(number)
        elif k[0] == 'U':
            number = int(k[1])
            Link.up(number)
        elif k[0] == 'C':
            addr = Link.c()
            address_stack.append(addr)
        else:
            addr = address_stack.pop()
            Link.z(addr)

    answer = Link.result(n)
    return answer

solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
# solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
