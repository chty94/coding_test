def solution(new_id):
    character = 'abcdefghijklmnopqrstuvwxyz'
    number = '1234567890'
    special = '-_.'

    new_id = new_id.lower()

    temp = ''
    for i in new_id:
        if (i in character) or (i in number) or (i in special):
            temp += i

    while '..' in temp:
        if ".." in temp:
            temp = temp.replace("..", ".")

    if temp[0] == '.' and temp[-1] == '.':
        temp = temp[1:-1]
    elif temp[0] == '.' and temp[-1] != '.':
        temp = temp[1:]
    elif temp[0] != '.' and temp[-1] == '.':
        temp = temp[:-1]

    if temp == '':
        temp = 'aaa'
        return temp

    if len(temp) >= 16:
        temp = temp[:15]
        while True:
            if temp[-1] == '.':
                temp = temp[:-1]
            else:
                break

    if len(temp) == 1:
        temp = temp + temp[-1] + temp[-1]
    elif len(temp) == 2:
        temp = temp + temp[-1]

    return temp
