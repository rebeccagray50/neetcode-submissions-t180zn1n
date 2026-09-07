class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 

        minPrice = prices[0]

        for i in range(len(prices)):
            #current lowest price 
            minPrice = min(prices[i], minPrice)
            #current profit
            profit = prices[i] - minPrice
            #update max 
            maxProfit = max(maxProfit, profit)
        
        return maxProfit
            