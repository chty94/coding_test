employee = {i: [] for i in range(300000)}
values = [[0, 0] for _ in range(300000)]


def solution(sales, links):
    for x, y in links:
        employee[x - 1].append(y - 1)
    for idx, value in enumerate(sales):
        values[idx][1] = value

    def traversal(parent):
        if employee[parent]:
            extravalue = float('inf')
            for child in employee[parent]:
                traversal(child)
                if values[child][1] > values[child][0]:
                    values[parent][0] += values[child][0]
                    values[parent][1] += values[child][0]
                    extravalue = min(extravalue, values[child][1] - values[child][0])
                else:
                    values[parent][0] += values[child][1]
                    values[parent][1] += values[child][1]
                    extravalue = 0
            values[parent][0] += extravalue
        else:
            return

    traversal(0)
    return min(values[0][0], values[0][1])