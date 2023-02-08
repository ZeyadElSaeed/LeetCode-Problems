class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        min_index = -1
        index = 0
        for point in points:
            if point[0] == x or point[1] == y:
                dist = abs(x-point[0]) + abs(y-point[1])
                if min_dist > dist:
                    min_dist = dist
                    min_index = index
            index += 1
        return min_index
                
        