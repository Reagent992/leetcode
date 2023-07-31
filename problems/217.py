"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/
Status: Solved.
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_nums = set()
        for i in nums:
            if i in last_nums:
                return True
            else:
                last_nums.add(i)
        else:
            return False


if __name__ == "__main__":
    nums = [1,2,3,4]
    solution = Solution()
    print(solution.containsDuplicate(nums))
