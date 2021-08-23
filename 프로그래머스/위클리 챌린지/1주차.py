def solution(price, money, count):
    need = price * count * (count + 1) / 2
    return need - money if need > money else 0