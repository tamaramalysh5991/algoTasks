from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        map_profit = 0
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[i]
            map_profit = map_profit + profit if profit > 0 else map_profit
        return map_profit
