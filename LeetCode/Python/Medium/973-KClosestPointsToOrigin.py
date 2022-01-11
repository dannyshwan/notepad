import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        pointDist = []
        heapq.heapify(pointDist)
        
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            
            heapq.heappush(pointDist, [distance, point])
            
        smallest = heapq.nsmallest(k, pointDist)

        ans = []
        for dist in smallest:
            ans.append(dist[1])
        return ans