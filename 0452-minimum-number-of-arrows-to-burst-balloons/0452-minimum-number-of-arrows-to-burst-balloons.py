class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points , key=lambda x: x[1])
        pointsLength = len(points) - 1
        numberOfArrows = 0
        pointIndex = 0
        groupList = list()

        if (pointsLength == 0):
            return 1

        #check the overlapping between intervals
        while pointIndex < pointsLength:
            startPoint = points[pointIndex]
            groupList.append(numberOfArrows)
            while pointIndex < pointsLength:
                pointIndex += 1
                endPoint = points[pointIndex]
                if (endPoint[0] > startPoint[1] or endPoint[1] < startPoint[0]):
                    break
                groupList.append(numberOfArrows)
            numberOfArrows += 1

        #check if the last point overlap with the previous point as edge case
        if ( len(points) != len(groupList) ):
                numberOfArrows += 1    

        return numberOfArrows