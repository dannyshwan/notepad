class SparseVector:
    vector = []
    length = 0
    def __init__(self, nums: List[int]):
        self.vector = nums
        self.length = len(nums)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        sum = 0
        for i in range(self.length):
            sum += self.vector[i]*vec.vector[i]
        return sum