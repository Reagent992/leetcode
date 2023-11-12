"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
Status: Solved
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    print(Solution().strStr("sadbutsad", "sad"))
    assert Solution().strStr("sadbutsad", "sad") == 0
    print(Solution().strStr("leetcode", "leeto"))
    assert Solution().strStr("leetcode", "leeto") == -1
