"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
Status: # TODO: Not Solved.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2=None):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        while list1:
            print(list1.val, end=" -> ")
            list1 = list1.next
        print("None")


if __name__ == '__main__':
    list1 = [1, 2, 4]
    first_node = ListNode(list1[-1])
    last_node = first_node
    for i in list1:
        t = ListNode(i, last_node)
        last_node = t

    print(Solution().mergeTwoLists(list1=last_node))
