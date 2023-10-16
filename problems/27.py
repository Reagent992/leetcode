"""
27. Remove Element
https://leetcode.com/problems/remove-element/description/
Result: Solved.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        left_index = 0
        for current_index in range(len(nums)):
            if nums[current_index] != val:
                nums[left_index] = nums[current_index]
                left_index += 1

        return left_index


if __name__ == "__main__":
    assert Solution().removeElement([3, 2, 2, 3], 3) == 2
    assert Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
