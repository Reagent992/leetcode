"""
1. Берем каждое число по очереди и складываем с оставшимися числами
пока в сумме не будет целевое число
"""

# ахаха, это одно из самых медленных решений на leetcode
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        variable1 = -1
        variable2 = 0
        for i1 in nums:
            variable1 += 1
            # ind1 = nums.index(i1)
            spare_nums = nums.copy()
            spare_nums.remove(i1)
            variable2 = 0
            for i2 in spare_nums:
                variable2 += 1
                if i1 + i2 == target:
                    return [variable1, variable2]
                    # ind2 = nums.index(i2)
                    # if ind1 != ind2:
                    #     return [ind1, ind2]
                    # else:
                    #     return 'это фиаско братан!'


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

    nums = [3, 2, 3]
    target = 6
    solution = Solution()
    print(solution.twoSum(nums, target))
