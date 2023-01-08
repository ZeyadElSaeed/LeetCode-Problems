class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pointsLength = len(points)
        maxPoints = 2

        if pointsLength == 1:
            return 1

        for i in range(pointsLength):
            AnglesDict = collections.defaultdict(int)
            for j in range(pointsLength):
                if j != i:
                    AnglesDict[math.atan2(points[j][1] - points[i][1],points[j][0] - points[i][0])] += 1
            maxPoints = max( maxPoints, max(AnglesDict.values()) + 1)

        return maxPoints        