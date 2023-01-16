from collections import Counter


def scramble(big, small):
#     for w in small:
#         n = big.find(w)
#         if n == -1:
#             return False
#         else:
#             big = big[:n] + big[n+1:]
#             print(big)
#
#     return True
    big_c = Counter(big)
    small_c = Counter(small)
    for char, count in small_c.items():
        if big_c[char] < count:
            return False
    return True

ans = scramble('rkqdolw', 'world')