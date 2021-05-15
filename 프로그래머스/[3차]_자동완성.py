def solution(words):
    class Node:
        def __init__(self, word):
            self.word = word
            self.next = dict()
            self.next_count = dict()

    class Trie:
        def __init__(self):
            self.head = Node(None)
            self.total = 0

        def insert(self, word):
            cur = self.head

            for i in range(len(word)):
                if cur.next.get(word[i]):
                    cur.next_count[word[i]] += 1
                    cur = cur.next[word[i]]
                else:
                    cur.next[word[i]] = Node(word[i])
                    cur.next_count[word[i]] = 1
                    cur = cur.next[word[i]]
            cur.next['#'] = Node('#')

        def result(self):
            stack = []
            cur = self.head
            for value in cur.next.values():
                stack.append([value, 1])

            while stack:
                cur, count = stack.pop()

                if cur.word == '#':
                    self.total += count - 1
                    continue

                if len(cur.next.keys()) == 1 and list(cur.next.keys())[0] != '#':
                    if list(cur.next_count.values())[0] == 1:
                        self.total += count
                        continue

                for key, value in cur.next.items():
                    stack.append([value, count + 1])

    auto = Trie()
    for word in words:
        auto.insert(word)

    auto.result()
    return auto.total

    
print(solution(["go","gone","guild"]))
print(solution(["abc", "def", "ghi", "jklm"]))
print(solution(	["word", "war", "warrior", "world"]))
