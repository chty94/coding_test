from collections import Counter


def solution(scores):
    answer = []
    student_number = len(scores)
    score_list = [[0] * student_number for _ in range(student_number)]

    for i in range(student_number):
        for j in range(student_number):
            score_list[j][i] = scores[i][j]

    for i in range(student_number):
        k = Counter(score_list[i])
        max_, min_ = max(score_list[i]), min(score_list[i])
        if min_ < scores[i][i] < max_:
            answer.append(sum(score_list[i]) / student_number)
        else:
            if k[scores[i][i]] == 1:
                answer.append((sum(score_list[i]) - score_list[i][i]) / (student_number - 1))
            else:
                answer.append(sum(score_list[i]) / student_number)

    real_answer = ''
    for average in answer:
        if average >= 90:
            real_answer += 'A'
        elif average >= 80:
            real_answer += 'B'
        elif average >= 70:
            real_answer += 'C'
        elif average >= 50:
            real_answer += 'D'
        else:
            real_answer += 'F'
    return real_answer