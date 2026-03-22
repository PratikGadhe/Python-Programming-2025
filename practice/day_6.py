# Write a Python Program to Add Two Matrices.
matrix1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
matrix2 = [
[9, 8, 7],
[6, 5, 4],
[3, 2, 1]
]
def addition(mat1 , mat2):
    if(len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0])):
        return "Matrices must have the same dimensions for addition"
    else :
        result = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat1[0])):
                row.append(mat1[i][j] + mat2[i][j])
            result.append(row)
        for row in result:
            print(row)
result = addition(matrix1,matrix2)


# Write a Python Program to Multiply Two Matrices.
matrix1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
matrix2 = [
[9, 8, 7],
[6, 5, 4],
[3, 2, 1]
]

def multiplication(mat1,mat2):
    row1 = len(mat1)
    cols1 = len(mat1[0])
    row2 = len(mat2)
    cols2 = len(mat2[0])
    if(cols1 != row2):
        return "Matrix multiplication is not possible."
    else :
        # result = []
        # for i in range(row1):
        #     row = []
        #     for j in range(cols2):
        #         row.append(0)
        #     result.append(row)
        # for row in result:
        #     print(row)
        result = [[0 for j in range(cols2)] for i in range(row1)]

        for i in range(row1):
            for j in range(cols2):
                for k in range(cols1):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        for i in result:
            print(i)
result = multiplication(matrix1,matrix2)
# print(result)

# Write a Python Program to Transpose a Matrix.
matrix = [
[1, 2, 3],
[4, 5, 6]
]
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    for i in result:
        print(i)
final = transpose(matrix)