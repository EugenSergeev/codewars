def max_sequence(numbers):
    if not any([True if num >= 0 else False for num in numbers ]):
        return 0
    max_summ = 0
    for i, num in enumerate(numbers):
        temp_summ = num
        max_summ = temp_summ if temp_summ > max_summ else max_summ
        for n in numbers[i+1:]:
            temp_summ += n
            max_summ = temp_summ if temp_summ > max_summ else max_summ
    return max_summ


a = max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])

