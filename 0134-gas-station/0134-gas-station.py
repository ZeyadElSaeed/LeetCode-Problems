class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        car_tank = 0
        total = 0
        myIndex = 0
        length = len(gas)

        for i in range(length):
            currentTank = gas[i] - cost[i]
            car_tank += currentTank
            total += currentTank
            if ( car_tank < 0 ):
                car_tank = 0
                myIndex = i + 1
        if ( total < 0):
            return -1
        else: 
            return myIndex