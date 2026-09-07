class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 

        #define current min
        minPrice = prices[0]
        
        for i in range(len(prices)):
            #if current is lower than min, update min
            minPrice = min(prices[i], minPrice)
            #calculate current profit
            profit = prices[i] - minPrice
            #if current profit > current max, update 
            maxProfit = max(profit, maxProfit)
        
        return maxProfit