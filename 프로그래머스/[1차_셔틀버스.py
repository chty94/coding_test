def TimeToSecond(time):
    HH, MM = time.split(':')
    second = int(HH)*60 + int(MM)
    return second

def SecondToTime(second):
    HH = second // 60
    MM = second % 60
    
    if HH <= 9:
        HH = '0' + str(HH)
    if MM <= 9:
        MM = '0' + str(MM)
            
    return str(HH) + ':' + str(MM)

def solution(n, t, m, timetable):   
    bus = dict()
    start = 9 * 60
    
    for i in range(n):
        bus[start] = []
        start += t
        
    timetable = [TimeToSecond(time) for time in timetable]
    timetable.sort()
    
    i = 0
    for key in bus.keys():
        while True:
            if i == len(timetable):
                break
            if timetable[i] > key or len(bus[key]) == m:
                break
            bus[key].append(timetable[i])
            i += 1
    
    key = list(bus.keys())[-1]
    list_ = bus[key]
    
    if len(list_) < m:
        return SecondToTime(key)
    else:
        return SecondToTime(list_[-1] - 1)
               

print(solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))