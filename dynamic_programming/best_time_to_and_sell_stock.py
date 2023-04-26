class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit
            else:
                l = r
            r += 1

        return max_profit

