"""
1. Берем каждое число по очереди и складываем с оставшимися числами
пока в сумме не будет целевое число
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i1 in nums:
            for i2 in nums:
                ...


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    print(solution.twoSum(nums, target))
    nums = [3, 3]
    target = 6
    solution = Solution()
    print(solution.twoSum(nums, target))
