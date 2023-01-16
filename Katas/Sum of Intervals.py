
# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    new_intervals = [intervals.pop(0)]
    while intervals:
        first_interval, second_interval = new_intervals[-1], intervals.pop(0)
        if first_interval[1] >= second_interval[0]:
            new_intervals[-1] = [min(first_interval[0], second_interval[0]), max(first_interval[1], second_interval[1])]
        else:
            new_intervals.append(second_interval)
    return sum(x[1] - x[0] for x in new_intervals)


intervals = [(7, 10), (1, 4), (3, 5)]

print(sum_of_intervals(intervals))
