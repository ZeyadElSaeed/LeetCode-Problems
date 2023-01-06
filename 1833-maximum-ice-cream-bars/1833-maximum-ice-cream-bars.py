class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        numberOfIceCreams = 0
        costs = sorted(costs)
        costsSum = 0

        for cost in costs:
            costsSum += cost
            if ( costsSum <= coins ):
                numberOfIceCreams += 1
            else :
                break

        return numberOfIceCreams        