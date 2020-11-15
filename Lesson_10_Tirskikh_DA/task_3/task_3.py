class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join([" ".join(map(lambda a: str(a), item)) for item in self.matrix])

    def __add__(self, other):
        new_list = []
        for i in range(0, len(self.matrix)):
            new_list.append([self.matrix[i][j] + other.matrix[i][j] for j in range(0, len(self.matrix[i]))])
        return Matrix(new_list)
