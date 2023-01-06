class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        numberOfIceCreams = 0
        costs = sorted(costs)

        for cost in costs:
            coins -= cost
            if ( coins >= 0 ):
                numberOfIceCreams += 1
            else :
                break

        return numberOfIceCreams        