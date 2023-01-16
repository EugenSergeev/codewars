# Snail - https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python

array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
array = [[1, 2, 3, 4, 5, 6],
            [20, 21, 22, 23, 24, 7],
            [19, 32, 33, 34, 25, 8],
            [18, 31, 36, 35, 26, 9],
            [17, 30, 29, 28, 27, 10],
            [16, 15, 14, 13, 12, 11]]


def snail(snail_map: list[list]):
    expected = []
    while snail_map:

        expected += snail_map.pop(0)

        if snail_map:
            expected += [row.pop(-1) for row in snail_map]

        if snail_map:
            expected += snail_map.pop(-1)[::-1]

        if snail_map:
            expected += [row.pop(0) for row in snail_map[::-1]]

    return expected


ans = snail(array)
print(ans, ans == expected)
