"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/description/
Status: Solved.
"""


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 5))
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
