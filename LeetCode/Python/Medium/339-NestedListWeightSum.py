class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth = 1
        sum = 0
        while nestedList:
            newList = []
            for el in nestedList:
                if el.isInteger():
                    sum += el.getInteger()*depth
                else:
                    newList += el.getList()
            nestedList = newList
            depth+=1
        return sum   