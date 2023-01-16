from time import time
from itertools import combinations_with_replacement


def getNumbers(user_number):
    answer = set()
    all_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    degree_cache = [i for i in range(10)]  # [0,1,2,3,4,5,6,7,8,9]

    user_number_razryadnost = len(str(user_number))
    for razryadnost in range(1, user_number_razryadnost + 1):
        if razryadnost > 1:
            for i in range(10):
                degree_cache[i] = degree_cache[i] * i
        for number in combinations_with_replacement(all_digits, razryadnost):
            sum = 0
            for d in number:
                sum += degree_cache[d]
            sum_digits = []
            for d in str(sum):
                sum_digits.append(int(d))
            if sorted(list(number)) == sorted(sum_digits):
                answer.add(sum)
    answer = sorted([i for i in answer if i < user_number])
    return answer[1:]


if __name__ == '__main__':
    t0 = time()
    user_number = 492927388522222

    print(getNumbers(user_number))
    print(f'Время выполнения - {time() - t0}')
