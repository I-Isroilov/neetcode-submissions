class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_profit = 0
        current_profit = 0

        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            current_profit = max(0, current_profit + diff)
            max_profit = max(max_profit, current_profit)

        return max_profit