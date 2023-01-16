# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python


def solution(strng, markers):
    print(f"{strng=}\n{markers=}")
    ans = []
    for row in strng.split("\n"):
        new_row = ""
        for l in row:
            if l in markers:
                break
            new_row += l
        ans.append(new_row.rstrip())
    ans = "\n".join(ans)
    print(f'{ans=}')
    return ans


a = solution('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
