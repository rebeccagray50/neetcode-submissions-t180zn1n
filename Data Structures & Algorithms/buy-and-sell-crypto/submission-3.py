class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 

        minPrice = prices[0]
        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)

            #calculate current profit 
            currentProfit = prices[i] - minPrice

            maxProfit = max(currentProfit, maxProfit)
        
        return maxProfit