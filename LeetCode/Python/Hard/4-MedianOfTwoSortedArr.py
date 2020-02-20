class Solution:
   def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
      combined = []
      ptr1, ptr2 = 0, 0
      even = True if (len(nums1) + len(nums2))%2 == 0 else False
      middle = (len(nums1) + len(nums2))//2 + 1
        
      while len(combined) != middle and ptr1 < len(nums1) and ptr2 < len(nums2):
                
         if nums1[ptr1] <= nums2[ptr2]:
            combined.append(nums1[ptr1])
            ptr1 += 1
                
         else:
            combined.append(nums2[ptr2])
            ptr2 += 1
          
      if ptr1 < len(nums1):
            self.appendRemainingEl(combined, ptr1, nums1, middle)
            
      if ptr2 < len(nums2):
            self.appendRemainingEl(combined, ptr2, nums2, middle)

      return (combined[-1] + combined[-2])/2 if even else combined[-1]
        
   def appendRemainingEl(self, combined, ptr, arr, middle) -> None:
            
      while len(combined) != middle and ptr < len(arr):
         combined.append(arr[ptr])
         ptr += 1