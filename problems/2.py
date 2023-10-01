"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
Stasut TODO: Not Solved
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    solution = Solution()
    t = solution.addTwoNumbers(l1, l2)
    print(t)
    assert t == [7, 0, 8]
