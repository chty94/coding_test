def solution(s):
    answer = ''

    WordToNumber = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    temp = ''
    for v in s:
        if v.isdigit():
            if temp != '':
                answer += WordToNumber[temp]
                temp = ''
            answer += v
        else:
            if WordToNumber.get(temp):
                answer += WordToNumber[temp]
                temp = ''
            temp += v
    if temp != '':
        answer += WordToNumber[temp]

    return int(answer)
print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
