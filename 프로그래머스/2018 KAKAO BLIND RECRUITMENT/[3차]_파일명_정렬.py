def solution(files):
    answer = []
    number = '0123456789'
    new_input = []

    for i, file in enumerate(files):
        HEAD, NUMBER, TAIL = '', '', ''
        step = 0
        for idx, value in enumerate(file):
            if step == 0:
                if value not in number:
                    HEAD += value
                else:
                    NUMBER += value
                    step += 1
            else:
                if len(NUMBER) == 5:
                    TAIL += file[idx:]
                    break
                elif value in number:
                    NUMBER += value
                else:
                    TAIL += file[idx:]
                    break

        new_input.append([HEAD.lower(), int(NUMBER), i, HEAD, NUMBER, TAIL])

    new_input.sort()
    for x, y, z, u, w, v in new_input:
        answer.append(u + w + v)

    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
