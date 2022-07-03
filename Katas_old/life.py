def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('\n')
    print(''.join(s))


start = [[1, 0, 0],
         [0, 1, 1],
         [1, 1, 0]]


end = [[0, 1, 0],
       [0, 0, 0],
       [0, 1, 1]]


def get_column(field, n):
    return [row[n] for row in field]


def delete_column(field, n):
    [row.pop(n) for row in field]


def get_generation(start, param):
    print("Начало")
    htmlize(start)
    f = Field(start)
    for i in range(1, param + 1):
        f.do_step()
    return f.array


class Field:
    def __init__(self, field):
        self.array = field
        self.steps = 0
        self.is_alive = self.check_live()

    @property
    def x_max(self):
        return len(self.array)

    @property
    def y_max(self):
        return len(self.array[0])

    def do_step(self):
        if not self.is_alive:
            return
        self.steps += 1
        print(f"Step {self.steps}")

        self._wraping_field()
        new_field = [[0] * self.y_max for _ in range(self.x_max)]
        for i, row in enumerate(self.array):
            for j, el in enumerate(row):
                neig_count = self.get_neigs(i, j)
                if el and neig_count in (3, 2):
                    new_field[i][j] = 1
                elif not el and neig_count == 3:
                    new_field[i][j] = 1
        self.array = new_field
        self.htmlize()
        if not self.check_live():
            print("Жизни больше нет((((")
            self.is_alive = False
        self._delete_empty_wrap()

    def _delete_empty_wrap(self):
        if self.is_alive == False:
            self.array = [[]]
            return
        while not any(self.array[0]):
            self.array.pop(0)
        while not any(self.array[-1]):
            self.array.pop(-1)
        while not any(get_column(self.array, 0)):
            delete_column(self.array, 0)
        while not any(get_column(self.array, -1)):
            delete_column(self.array, -1)

    def get_neigs(self, x, y):
        neigs = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if not (i < 0 or i > self.x_max - 1 or j < 0 or j > self.y_max - 1 or i == x and j == y):
                    neigs += self.array[i][j]
        return neigs

    def _wraping_field(self):
        new_array = [[0] * (self.y_max + 2) for _ in range(self.x_max + 2)]
        for i in range(1, self.x_max + 1):
            for j in range(1, self.y_max + 1):
                new_array[i][j] = self.array[i - 1][j - 1]
        self.array = new_array
        # self.htmlize()

    def htmlize(self):
        s = []
        for row in self.array:
            for cell in row:
                s.append('▓▓' if cell else '░░')
            s.append('\n')
        print(''.join(s))

    def check_live(self):
        return True if any(any(row) for row in self.array) else False


resp = get_generation(start, 1)
pprint(resp)
