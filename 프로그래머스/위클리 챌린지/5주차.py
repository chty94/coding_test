dictionary = []


def dfs(word):
    global dictionary

    dictionary.append(word)

    if len(word) == 5:
        return

    for x in ["A", "E", "I", "O", "U"]:
        dfs(word + x)


def solution(word):
    dfs("")
    dictionary.sort()
    return dictionary.index(word)