class Solution:
   def sortByBits(self, arr: List[int]) -> List[int]:
      bits = {}
      binarySort = []
        
      for n in arr:
         print(bin(n)[2:])
         temp = bin(n)[2:].count('1')    
         if not bits.get(temp):
            bits[temp] = []
            bits[temp].append(n)
            
         else:
            bits[temp].append(n)
        
      keyOrder = sorted(bits.keys())
      for key in keyOrder:
         bits[key].sort()
         binarySort += bits[key]

      return binarySort