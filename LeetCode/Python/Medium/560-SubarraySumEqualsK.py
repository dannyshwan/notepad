class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cSum = 0
        preSum = {}
        preSum[0] = 1

        for num in nums:
            cSum += num
            rSum = cSum - k
            res += preSum.get(rSum, 0)
            preSum[cSum] = 1 + preSum.get(cSum, 0)
        return res