class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        resultProfit = 0
        profit = 0
        j = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[j]:
                profit = prices[i] - prices[j]
                resultProfit += profit
            j += 1

        return resultProfit

