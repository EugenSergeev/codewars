# https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python

triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

answer = ''

while any(triplets):
    letter_ranks = {}
    for trip in triplets:
        for i, l in enumerate(trip):
            letter_ranks.setdefault(l, 0)
            letter_ranks[l] += i
    first_l = [l for l, c in letter_ranks.items() if c == 0][0]
    answer += first_l
    [trip.remove(first_l) for trip in triplets if first_l in trip]


