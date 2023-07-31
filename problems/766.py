"""
766. Toeplitz Matrix
https://leetcode.com/problems/toeplitz-matrix/
Верно.
"""


class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        matrix_item_len = len(matrix[0]) - 1
        matrix_len = len(matrix) - 1
        result = 'true'

        for current_matrix in range(matrix_len):
            for item_index in range(matrix_item_len):
                new_item = item_index + 1
                new_current_matrix = current_matrix + 1
                if (new_item <= matrix_item_len and
                        new_current_matrix <= matrix_len):
                    if (matrix[current_matrix][item_index] !=
                            matrix[new_current_matrix][new_item]):
                        result = 'fail'
                        return result

        return result


if __name__ == '__main__':
    # matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    matrix = [[1, 2], [2, 2]]
    solution = Solution()
    print(solution.isToeplitzMatrix(matrix=matrix))
