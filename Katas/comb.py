from itertools import combinations_with_replacement

digits = [0,1,2,3,4,5,6,7,8,9]

all_numbers = []
for razr in range(1, 17):
    a = list(combinations_with_replacement(digits, razr))
    all_numbers += a