class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        indices = []
        max = 0
        
        for i, num in reversed(list(enumerate(heights))):
            
            if num > max:
                indices.append(i)
                max = num
                
        return reversed(indices)