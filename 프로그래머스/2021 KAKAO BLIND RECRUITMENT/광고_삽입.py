def convert(time):
    nums = time.split(':')
    return int(nums[0]) * 60 * 60 + int(nums[1]) * 60 + int(nums[0])


def solution(play_time, adv_time, logs):
    playSec = convert(play_time)
    advSec = convert(adv_time)

    totalSec = [0 for _ in range(100 * 3600)]

    for log in logs:
        start = convert(log[:8])
        end = convert(log[9:])

        for i in range(start, end):
            totalSec[i] += 1

    currSum = 0
    for i in range(advSec):
        currSum += totalSec[i]

    maxSum = currSum
    maxIdx = 0
    for i in range(advSec, playSec):
        if i - advSec + 1 == 5455:
            k = 1
        currSum = currSum + totalSec[i] - totalSec[i - advSec]
        if currSum > maxSum:
            maxSum = currSum
            maxIdx = i - advSec + 1

    return "%02d:%02d:%02d" % (maxIdx // 3600, maxIdx // 60 % 60, maxIdx % 60)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
