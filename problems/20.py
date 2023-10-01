"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
Status: Solved.
"""


class Solution(object):
    def isValid(self, s):
        left_parentheses = ['{', '[', '(']
        parentheses = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        storage = []
        for item in s:
            if item in left_parentheses:
                storage.append(item)
            else:
                compared_item = parentheses.get(item)
                if compared_item in storage:
                    last_in_storage = storage.pop()
                    if compared_item == last_in_storage:
                        continue
                    else:
                        return False
                else:
                    return False

        if not storage:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "]"
    print(Solution().isValid(s=s))
