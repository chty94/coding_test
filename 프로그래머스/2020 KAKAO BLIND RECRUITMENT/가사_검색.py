def solution(words, queries):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = dict()
            self.next_count = dict()

    class Trie:
        def __init__(self):
            self.head = Node(None)

        def insert(self, word):
            cur = self.head
            for w in word:
                if w in cur.next:
                    cur.next_count[w] += 1
                    cur = cur.next[w]
                else:
                    cur.next[w] = Node(w)
                    cur.next_count[w] = 1
                    cur = cur.next[w]

        def find(self, word):
            total = 0

            cur = self.head
            for w in word:
                if w == '?':
                    for value in cur.next_count.values():
                        total += value
                    return total

                if w in cur.next:
                    cur = cur.next[w]
                else:
                    return 0

    all_case = [Trie() for _ in range(10001)]
    all_reverse_case = [Trie() for _ in range(10001)]

    for word in words:
        length = len(word)

        all_case[length].insert(word)
        all_reverse_case[length].insert(word[::-1])

    answer = []
    for query in queries:
        length = len(query)

        if query[0] == '?':
            answer.append(all_reverse_case[length].find(query[::-1]))
        else:
            answer.append(all_case[length].find(query))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
