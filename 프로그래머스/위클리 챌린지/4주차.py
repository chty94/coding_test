def solution(table, languages, preference):
    answer = ''

    t = {
        "SI": {"JAVA" : 0, "JAVASCRIPT": 0, "C": 0, "C++": 0, "C#": 0, "SQL": 0, "PYTHON": 0, "KOTLIN": 0, "PHP": 0},
        "CONTENTS": {"JAVA" : 0, "JAVASCRIPT": 0, "C": 0, "C++": 0, "C#": 0, "SQL": 0, "PYTHON": 0, "KOTLIN": 0, "PHP": 0},
        "HARDWARE": {"JAVA" : 0, "JAVASCRIPT": 0, "C": 0, "C++": 0, "C#": 0, "SQL": 0, "PYTHON": 0, "KOTLIN": 0, "PHP": 0},
        "PORTAL": {"JAVA" : 0, "JAVASCRIPT": 0, "C": 0, "C++": 0, "C#": 0, "SQL": 0, "PYTHON": 0, "KOTLIN": 0, "PHP": 0},
        "GAME": {"JAVA" : 0, "JAVASCRIPT": 0, "C": 0, "C++": 0, "C#": 0, "SQL": 0, "PYTHON": 0, "KOTLIN": 0, "PHP": 0}
    }

    jobs = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]
    for temp in table:
        job, five, four, three, two, one = temp.split()
        t[job][five] = 5
        t[job][four] = 4
        t[job][three] = 3
        t[job][two] = 2
        t[job][one] = 1


    score_list = []
    for job in jobs:
        temp = 0
        for idx, language in enumerate(languages):
            temp += t[job][language] * preference[idx]
        score_list.append([-temp, job])
    score_list.sort()

    return score_list[0][1]
