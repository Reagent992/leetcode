"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Status: Solved.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 0
        for cur_index in range(1, len(nums)):
            if nums[cur_index] != nums[index]:
                nums[index + 1] = nums[cur_index]
                index += 1
        return len(nums[: index + 1])


if __name__ == "__main__":
    assert Solution().removeDuplicates([1, 1, 2]) == 2
    assert Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
