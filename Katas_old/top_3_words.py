from itertools import product


def get_neigs(n):
    keyboard = [['1', '2', '3'],
                ['4', '5', '6'],
                ['7', '8', '9'],
                ['', '0', '']]
    for i, row in enumerate(keyboard):
        for j, el in enumerate(row):
            if n == el:
                r, c = i, j
    neigs = [n]
    try:
        r_ = r - 1
        if r_ < 0:
            raise IndexError
        neigs.append(keyboard[r_][c])
    except IndexError:
        pass
    try:
        neigs.append(keyboard[r + 1][c])
    except IndexError:
        pass
    try:
        c_ = c - 1
        if c_ < 0:
            raise IndexError
        neigs.append(keyboard[r][c_])
    except IndexError:
        pass
    try:
        neigs.append(keyboard[r][c + 1])
    except IndexError:
        pass
    return [n for n in neigs if n]


def get_pins(nums):
    return ["".join(s) for s in list(product(*[get_neigs(n) for n in nums]))]

nums = '11'
print(get_pins(nums))



>987v>.v
v456<  :
>321 ^ _@