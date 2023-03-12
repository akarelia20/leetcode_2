class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l= 0 
        r = 1
        while r <= len(prices)-1:
#            if profit
            if prices[l] < prices[r]:
                profit= max(profit, prices[r]-prices[l])
#                 if no profit
            elif (prices[r] - prices[l]) < profit:
                l = r
#             right pointer will move +1 every iteration
            r+= 1
            
        return profit
           
            
        