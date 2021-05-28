def solution(numbers):
    answer = []
    for number in numbers:
        if number & 1 == 1: # 홀수
            k = 0
            while True:
                if number & (1 << k) == 0:
                    answer.append(number + (1 << k) - (1 << (k - 1)))
                    break
                k += 1
        else: # 짝 수
            answer.append(number + 1)
    return answer
