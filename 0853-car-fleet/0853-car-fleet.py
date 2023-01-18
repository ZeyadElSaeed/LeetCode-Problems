class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine_list = list()
        fromTarget = list()
        answer = 0
        for x,y in zip( position , speed ):
            combine_list.append( (x,y) )
        combine_list = sorted( combine_list )
        for (x,y) in combine_list:
            fromTarget.append((target - x) / y)

        fromTarget = [target] + fromTarget
        print( fromTarget )
        i = len(fromTarget) - 1
        while( i > 0):
            if ( fromTarget[i] < fromTarget[i-1]):
                answer += 1
                i -= 1
            else:
                x = fromTarget[i]
                i -= 1
                while( i > 0 and x >= fromTarget[i]):
                    i -= 1
                answer += 1    

        return answer