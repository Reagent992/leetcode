"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
Status: Solved
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        len_s = len(s)
        result = 0

        for index in range(len_s - 1):
            cur_rom = s[index]
            if roman_dict[cur_rom] < roman_dict[s[index + 1]]:
                result -= roman_dict[cur_rom]
            else:
                result += roman_dict[cur_rom]
        return result + roman_dict[s[-1]]
            

if __name__ == "__main__":
    solution = Solution()
    s = "MCMXCIV"
    print(solution.romanToInt(s), 'must be 1994')
