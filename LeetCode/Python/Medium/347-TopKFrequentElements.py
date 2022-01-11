import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        setNums = set(nums)
        heap = []
        heapq.heapify(heap)
        ans = []
        
        for num in setNums:
            count = nums.count(num)
            heapq.heappush(heap, (count, num))
            
        kLargests = heapq.nlargest(k, heap)
        for num in kLargests:
            ans.append(num[-1])
            
        return ans