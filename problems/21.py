"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
Status: Solved.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        tail = head = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next
        if list1 or list2:
            tail.next = list1 if list1 else list2
        return head.next


if __name__ == '__main__':
    n3 = ListNode(val=4)
    n2 = ListNode(val=2, next=n3)
    n1 = ListNode(val=1, next=n2)
    l3 = ListNode(val=4)
    l2 = ListNode(val=3, next=l3)
    l1 = ListNode(val=1, next=l2)


    def print_linked_list(vertex):
        while vertex:
            print(vertex.val, end=" -> ")
            vertex = vertex.next
        print("The End")


    print_linked_list(Solution().mergeTwoLists(list1=n1, list2=l1))
