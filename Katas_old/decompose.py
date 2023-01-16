from math import sqrt

def f(list, summ):
    if summ == 0:
        return list
    list = list[:]
    new_n = sqrt(summ) // 1
    if not list:
        new_n -= 1
    if list and new_n >= list[-1]:
        # return False
        new_n = list[-1]-1
        if new_n in (0,1):
            return False
    while new_n > 0:
        list.append(new_n)
        new_summ = summ - new_n ** 2
        new_list = f(list, new_summ)
        if new_list:
            return new_list
        else:
            new_n -= 1
            list = list[:-1]
    return new_list if new_n else False


def decompose(n):
    list_ = f([], n ** 2)
    list_ = list_[::-1] if list_ else None
    return list_


n = 221503
summ = n ** 2

print(decompose(n))
