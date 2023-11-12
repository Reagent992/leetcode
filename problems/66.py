"""
66. Plus One
https://leetcode.com/problems/plus-one/description/
Status: Solved.
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join([str(i) for i in digits])) + 1
        return [int(i) for i in str(number)]


if __name__ == "__main__":
    print(Solution().plusOne([1, 2, 3]))
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
