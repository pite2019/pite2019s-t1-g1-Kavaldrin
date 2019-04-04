from Matrix import Matrix, RandomMatrixGenerator

if __name__ == '__main__':

    matrix = Matrix(2)
    print(matrix)
    matrix2 = matrix + 4
    matrix3 = 2 + matrix2
    matrix4 = matrix3 + matrix2
    print(matrix4)

    matrix4 = Matrix(3, *[[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    print(matrix4)
    matrix5 = 1 - matrix4
    print(matrix5)
    matrix6 = matrix5 - 4
    print(matrix6)
    matrix7 = matrix5 - matrix6
    print(matrix7)

    matrix7 += matrix7
    print(matrix7)
    matrix7 += 2
    print(matrix7)

    matrix8 = matrix7 @ matrix7
    print(matrix8)

    gen = RandomMatrixGenerator(4, 1, 5)
    print(next(gen))
    print(next(gen))
