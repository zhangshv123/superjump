# Generate a random MxN starting board. It cannot have 3 or more pieces in a row (horizontally or vertically) of the same color. K colors.
import random
def generateColorMatrix(M, N, colors):
    matrix = [[0 for _ in range(N)] for _ in range(M)]
    def isValid(i, j, color):
        if i > 2 and matrix[i - 1][j] == color and matrix[i - 2][j] == color:
            return False
        if j > 2 and matrix[i][j - 1] == color and matrix[i][j - 2] == color:
            return False
        return True
    for i in range(M):
        for j in range(N):
            while True:
                color = random.choice(colors)
                if isValid(i, j, color):
                    matrix[i][j] = color
                    break
    return matrix
print(generateColorMatrix(5, 5, ['r', 'b', 'y']))