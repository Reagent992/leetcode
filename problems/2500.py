"""
2500. Delete Greatest Value in Each Row
https://leetcode.com/problems/delete-greatest-value-in-each-row/
Status: Solved. Fast.
"""


class Solution:
    def deleteGreatestValue(self, grid):
        len_of_array = len(grid[0])
        answer = 0

        for _ in range(len_of_array):
            items = []

            for array in grid:
                max_item = max(array)
                items.append(max_item)
                array.remove(max_item)

            answer += max(items)

        return answer


if __name__ == '__main__':
    grid = [[1, 2, 4], [3, 3, 1]]
    solution = Solution()
    print(solution.deleteGreatestValue(grid))
