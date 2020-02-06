class Solution:
   def findKthLargest(self, nums: List[int], k: int) -> int:
        
      rank = nums
                
      rank.sort()
      return rank[-1*k]