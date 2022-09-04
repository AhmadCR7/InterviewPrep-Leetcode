class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
                
        return profit 
        
        
        
        
'''

since we can predect the fucture we can see when to buy or sell
profit = 0
pointer i we ignore the first value for i in range(1, len(prices))
if prices[i] > prices[i-1]
calculate the profite profit += (prices[i] - prices[i-1])
return profit 

'''