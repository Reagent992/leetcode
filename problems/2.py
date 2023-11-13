"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
Status: Solved.
"""
from typing import List, Optional
from itertools import zip_longest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def list_node_to_int(self, node: Optional[ListNode]) -> int:
        array = []
        cur_node = node
        while cur_node is not None:
            array.append(int(cur_node.val))
            cur_node = cur_node.next
        return array

    def create_node_list(self, item: List[int]) -> ListNode:
        last = None
        for i in item[::-1]:
            last = ListNode(i, last)
        return last

    def sum_to_list_of_ints(self, first_list, second_list):
        result = []
        rest = 0
        for i in zip_longest(first_list, second_list, fillvalue=0):
            t = sum(i) + rest
            if t >= 10:
                rest = 1
                result.append(t % 10)
            else:
                result.append(t)
                rest = 0
        if rest:
            result.append(rest)
        return result

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first_list = self.list_node_to_int(l1)
        second_list = self.list_node_to_int(l2)
        t = self.sum_to_list_of_ints(first_list, second_list)
        return self.create_node_list(t)


if __name__ == "__main__":
    # l1_prep4 = ListNode(3, None)
    l1_prep3 = ListNode(3, None)
    l1_prep2 = ListNode(4, l1_prep3)
    l1_prep1 = ListNode(2, l1_prep2)
    l1 = l1_prep1
    l2_prep3 = ListNode(4, None)
    l2_prep2 = ListNode(6, l2_prep3)
    l2_prep1 = ListNode(5, l2_prep2)
    l2 = l2_prep1
    t = Solution().addTwoNumbers(l1, l2)
    print(t)
    print(t.val)
    test_on = True
    if test_on:
        assert t.val == 7
        assert t.next.val == 0
        assert t.next.next.val == 8
