class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for i in range(l):
            for j in range(i, l):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for i in range(l):
            for j in range(0, l // 2, 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][l - 1 - j]
                matrix[i][l - 1 - j] = temp