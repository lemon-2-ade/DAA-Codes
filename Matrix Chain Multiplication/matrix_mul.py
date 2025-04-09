def matrix_product(x: list[list[int]], y: list[list[int]]):
    col_x = len(x[0])
    row_y = len(y)

    if not col_x == row_y:
        raise ValueError("Wrong order of matrices!")

    # allocating memory for the resulting array
    result = [[0] * len(y[0]) for i in range(len(x))]
    k = 0
    
    for i in range(len(x)):
        for j in range(len(y)):
            for k in range():
                result[i][j] += x[i][k] * y[k][j]
    
    print(result)

if __name__ == "__main__":
    matrix_a = [
        [34, 56, 67],
        [87, 10, 19]
    ]

    matrix_b = [
        [10, 19],
        [18, -12],
        [30, -18]
    ]

    try:
        matrix_product(matrix_b, matrix_a)
    except ValueError as error:
        print(error)