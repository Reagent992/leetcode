"""
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
Status: Solved.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            last = head
            cur = head
            while cur:
                if cur.val > last.val:
                    last.next = cur
                    last = cur
                cur = cur.next
            last.next = None
        return head


if __name__ == '__main__':
    a3 = ListNode(2)
    a2 = ListNode(1, a3)
    a1 = ListNode(1, a2)
    b5 = ListNode(3)
    b4 = ListNode(3, b5)
    b3 = ListNode(2, b4)
    b2 = ListNode(1, b3)
    b1 = ListNode(1, b2)


    def print_linked_list(vertex):
        while vertex:
            print(vertex.val, end=" -> ")
            vertex = vertex.next
        print("The End")


    t = Solution().deleteDuplicates(a1)
    t2 = Solution().deleteDuplicates(b1)
    print_linked_list(t)
    print_linked_list(t2)
