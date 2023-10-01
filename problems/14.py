"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
Status: Solved
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        answer = ''
        first_word = strs[0]
        if not len(first_word) > 0:
            return answer
        if len(strs) == 1:
            return first_word
        counter = 1
        answer = first_word[:counter]
        while counter <= len(first_word):
            for word in strs:
                if word[:counter] == answer[:counter]:
                    continue
                else:
                    return first_word[:counter - 1]
            counter += 1
            answer = first_word[:counter + 1]
        else:
            return answer


if __name__ == '__main__':
    strs = ["dxgf", "dogs", "dogq"]
    print(Solution().longestCommonPrefix(strs=strs))
