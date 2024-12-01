import random

class Matrix:
    def __init__(self, x, y):
        self.create_matrix(x, y)

    def create_matrix(self, x, y):
        matrix = []
        for i in range(x):
            row = []
            for j in range(y):
                row.append(random.randint(0, 10))  
            matrix.append(row) 
        self.matrix = matrix

    def print_matrix(self):
        for row in self.matrix:
            print(row)

    def get_row_sum(self, index):
        return sum(self.matrix[index])  

    def print_submatrix(self, row1, row2, col1, col2):
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                print(self.matrix[i][j], end=" ")
            print()



matrix = Matrix(4, 5) 
matrix.print_matrix() 

print("Sum of row 2:", matrix.get_row_sum(2)) 
print("Submatrix (1,1) to (3,3):")

matrix.print_submatrix(1, 3, 1, 3) 
