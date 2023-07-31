"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
Stastus: Я не понимаю условия, там какой-то свой класс, ListNode, я просто не понимаю как он работает.
"""
"""     first version:
        first_reversed_array = l1[::-1]
        second_reversed_array = l2[::-1]
        first_str = ""
        second_str = ""
        for i in first_reversed_array:
            first_str += str(i)
        for i in second_reversed_array:
            second_str += str(i)
        half_result = int(first_str) + int(second_str)
        result = list(str(half_result))[::-1]
        return list(map(int, result))
        """
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # TODO: переделать ввод, l1 - ListNode

        


if __name__ == "__main__":
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))


inpt = input().split()
d = dict()
for i in inpt:
    key,value = i.split('=')
    d[str(key)] = int(value)

print(*sorted(d.items()))