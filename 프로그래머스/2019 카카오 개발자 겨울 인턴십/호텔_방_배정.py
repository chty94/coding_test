import sys
sys.setrecursionlimit(100000)

def solution(k, room_number):
    def find(room_dict, room):
        if room not in room_dict:
            room_dict[room] = room + 1
            return room

        empty = find(room_dict, room_dict[room])
        room_dict[room] = empty + 1
        return empty

    room_dict = dict()
    result = []
    for room in room_number:
        number = find(room_dict, room)
        result.append(number)

    return result

print(solution(10, [1, 3, 4, 1, 3, 1]))
