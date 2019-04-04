from random import randint


class Matrix:
    def __init__(self, size, *initial_data):
        self.size = size
        if initial_data:
            self.memory = [[elem for elem in row] for row in initial_data]
        else:
            self.memory = [[0 for _ in range(size)] for _ in range(size)]

    def __add__(self, argument):
        if isinstance(argument, float) or isinstance(argument, int):
            new_matrix = Matrix(self.size)
            for i in range(self.size):
                for j in range(self.size):
                    new_matrix.memory[i][j] = self.memory[i][j] + argument
            return new_matrix
        elif isinstance(argument, Matrix) and argument.size == self.size:
            if argument.size == self.size:
                new_matrix = Matrix(self.size)
                for i in range(self.size):
                    for j in range(self.size):
                        new_matrix.memory[i][j] = self.memory[i][j] + argument.memory[i][j]
                return new_matrix
        else:
            raise TypeError()

    def __radd__(self, argument):
        return self + argument

    def __iadd__(self, argument):
        if isinstance(argument, float) or isinstance(argument, int):
            for i in range(self.size):
                for j in range(self.size):
                    self.memory[i][j] += argument
            return self
        elif isinstance(argument, Matrix) and argument.size == self.size:
            if argument.size == self.size:
                for i in range(self.size):
                    for j in range(self.size):
                        self.memory[i][j] += argument.memory[i][j]
            return self

    def __sub__(self, argument):
        if isinstance(argument, float) or isinstance(argument, int):
            new_matrix = Matrix(self.size)
            for i in range(self.size):
                for j in range(self.size):
                    new_matrix.memory[i][j] = self.memory[i][j] - argument
            return new_matrix
        elif isinstance(argument, Matrix) and argument.size == self.size:
            if argument.size == self.size:
                new_matrix = Matrix(self.size)
                for i in range(self.size):
                    for j in range(self.size):
                        new_matrix.memory[i][j] = self.memory[i][j] - argument.memory[i][j]
                return new_matrix
        else:
            raise TypeError()

    def __rsub__(self, argument):
        return self - argument

    def __matmul__(self, argument):
        if isinstance(argument, Matrix):
            new_matrix = Matrix(self.size)
            for i in range(self.size):
                for j in range(self.size):
                    sum_val = 0
                    for k in range(self.size):
                        sum_val += self.memory[i][k] * self.memory[k][j]
                    new_matrix.memory[i][j] = sum_val
            return new_matrix
        else:
            raise TypeError()

    def __str__(self):
        output = ''.join("Printing matrix:\n")
        for row in self.memory:
            for elem in row:
                output += "{" + str(elem) + "]"
            output += "\n"
        return output


class RandomMatrixGenerator:
    def __init__(self, size, min_val, max_val):
        self.size = size
        self.min_val = min_val
        self.max_val = max_val

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        while True:
            new_matrix = Matrix(self.size)
            for i in range(self.size):
                for j in range(self.size):
                    new_matrix.memory[i][j] = randint(self.min_val, self.max_val)
            return new_matrix
