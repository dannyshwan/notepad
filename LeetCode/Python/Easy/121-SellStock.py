'''
Pretty meh solution, might fix later lol
'''
class Solution:
   def maxProfit(self, prices: List[int]) -> int:
        
      maxProfit = 0
      if not prices:
         return maxProfit
        
      for i in range(len(prices)):
            
         j = i+1
         if j == len(prices):
            return maxProfit
            
         else:  
            if max(prices[j:]) - prices[i] > maxProfit:
               maxProfit = max(prices[j:]) - prices[i]