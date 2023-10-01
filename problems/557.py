"""
557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/?envType=daily-question&envId=2023-10-01
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        for word in s.split():
            answer.append(word[::-1])
        return ' '.join(answer)


if __name__ == '__main__':
    s = Solution()
    t = s.reverseWords("Let's take LeetCode contest")
    assert t == "s'teL ekat edoCteeL tsetnoc"
