class error(Exception):
    pass


class User:

    def __init__(self):
        self._progress = 0
        self._rank = -8

    @property
    def rank(self):
        return self._rank

    @property
    def progress(self):
        if self.rank == 8:
            return 0
        return self._progress

    @progress.setter
    def progress(self, value):
        print(f'{self.rank}-{self.progress}+{value - self.progress}')
        if value // 100:
            self.up_runk(value // 100)
        self._progress = value % 100
        print(f'{self.rank}-{self.progress}')

    def inc_progress(self, task_rank):
        if -8 > task_rank or task_rank > 8 or task_rank == 0:
            raise error
        print(f'{self.rank=}, {task_rank=}')
        if self.rank < 0 and task_rank > 0:
            task_rank -= 1
        if self.rank > 0 and task_rank < 0:
            task_rank += 1
        rank_delta = task_rank - self.rank
        if rank_delta == -1:
            self.progress = self.progress + 1
        elif rank_delta == 0:
            self.progress = self.progress + 3
        elif rank_delta > 0:
            self.progress = self.progress + 10 * rank_delta ** 2

    def up_runk(self, n):
        if self.rank < 0 and (self.rank + n) >= 0:
            n += 1
        self._rank += n
        if self.rank > 7:
            self._rank = 8
            self._progress = 0
