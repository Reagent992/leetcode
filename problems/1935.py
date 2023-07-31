"""
1935. Maximum Number of Words You Can Type
https://leetcode.com/problems/maximum-number-of-words-you-can-type/
Результат: Верно.
"""


class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        result = 0

        split_text = text.split()
        brokenLetters = list(brokenLetters)
        for word in split_text:
            t = False
            for letter in brokenLetters:
                if letter in word:
                    t = True
            if t:
                result += 1

        return len(split_text) - result


if __name__ == '__main__':
    text = 'leet code'
    brokenLetters = 'e'
    solution = Solution()
    print(solution.canBeTypedWords(text, brokenLetters))
