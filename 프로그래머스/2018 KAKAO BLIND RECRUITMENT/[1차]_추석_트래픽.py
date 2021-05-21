def solution(lines):
    bar = []
    result = []
    for idx, line in enumerate(lines):
        endTime = line.split()[1]
        delay = int(float(line.split()[2][:-1])*1000)

        temp = endTime.split(':')
        total = int(int(temp[0])*3600*1000 + int(temp[1])*60*1000 + float(temp[2])*1000)

        # print(total, delay)

        bar.append([total-delay+1, total])

    for b in bar:
        count = 0
        start = b[0]
        end = b[0]+999
        for c in bar:
            if c[1] >= start and c[0] <= end:
                count += 1
        result.append(count)

        count = 0
        start = b[0]-999
        end = b[0]
        for c in bar:
            if c[1] >= start and c[0] <= end:
                count += 1
        result.append(count)
        
        count = 0
        start = b[1]
        end = b[1]+999
        for c in bar:
            if c[1] >= start and c[0] <= end:
                count += 1
        result.append(count)
        
        count = 0
        start = b[1]-999
        end = b[1]
        for c in bar:
            if c[1] >= start and c[0] <= end:
                count += 1
        result.append(count)
        
    # 1초는 1000
    return max(result)

print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
