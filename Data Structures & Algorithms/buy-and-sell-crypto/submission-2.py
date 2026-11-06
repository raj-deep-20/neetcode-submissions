class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' DP
        minPrice = prices[0]
        maxProfit = 0
        for sell in prices:
            maxProfit = max(maxProfit, sell - minPrice)
            minPrice = min(minPrice, sell)
        return maxProfit '''

        l=0
        r=1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP
