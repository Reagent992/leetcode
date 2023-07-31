"""
1518. Water Bottles
https://leetcode.com/problems/water-bottles/
Статус: Верно.
"""


class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        drunk_bottles = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            # Меняем пустые на полные
            filled_bottles = empty_bottles // numExchange
            # Записываем новые в выпитые
            drunk_bottles += filled_bottles
            # Обновляем кол-во пустых банок.
            empty_bottles = (empty_bottles - filled_bottles
                             * numExchange + filled_bottles)

        return drunk_bottles


if __name__ == '__main__':
    numBottles = 9
    numExchange = 3
    solution = Solution()
    print(solution.numWaterBottles(numBottles, numExchange))
