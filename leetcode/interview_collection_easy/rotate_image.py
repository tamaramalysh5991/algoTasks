from typing import List

matrix = [[1,2,3],[4,5,6],[7,8,9]]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

        # return matrix

print(Solution().rotate(matrix))
print(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)