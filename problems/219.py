"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/
Статус: Верно.
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        past_nums = {}
        for index, num in enumerate(nums):
            if num in past_nums and abs(index - past_nums.get(num)) <= k:
                return True
            else:
                past_nums[num] = index
        else:
            return False


if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums, k))
