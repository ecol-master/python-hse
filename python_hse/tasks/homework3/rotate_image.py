"""
Task info:
https://leetcode.com/problem-list/array
url: https://leetcode.com/problems/rotate-image/description
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            for j in range(len(matrix) // 2):
                matrix[i][j], matrix[i][len(matrix) - j - 1] = (
                    matrix[i][len(matrix) - j - 1],
                    matrix[i][j],
                )
