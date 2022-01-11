import numpy
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = -numpy.inf
        peakIndice = -1
        peaks = []
        
        if len(nums) == 1:
            return 0
        
        for i, num in enumerate(nums):
            if num < peak:
                peaks.append(i-1)
            peak = num
            peakIndice = i
        
        peaks.append(i)
        return peaks.pop(0)