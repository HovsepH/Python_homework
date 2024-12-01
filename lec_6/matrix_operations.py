import random

def generate_random_matrix(rows, cols):
    matrix = []

    for i in range(0, rows):
        row = []
        for j in range(0, cols):
            row.append(random.randint(1, 100))
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def get_column_sum(matrix, col_index):
    sum = 0
    for row in matrix:
        sum += row[col_index]
    return sum

def get_row_average(matrix, row_index):
    sum = 0
    for i in matrix[row_index]:
        sum += i
    return sum/len(matrix[row_index])


matrix = generate_random_matrix(2,2)
print_matrix(matrix)
print(get_column_sum(matrix, 0))
print(get_row_average(matrix, 0))