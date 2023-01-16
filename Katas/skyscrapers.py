# - https://www.codewars.com/kata/5671d975d81d6c1c87000022/train/python


class Map:
    def __init__(self, clues: list[list]):
        self.clues = clues
        self.map = [[Tower() for _ in clues[0]] for _ in clues]


class Tower:
    def __init__(self):
        self.height = None
        self.options = []


def solve_puzzle (clues):
    return ( (1, 2, 3, 4), (2, 3, 4, 1), (3, 4, 1, 2), (4, 1, 2, 3) )