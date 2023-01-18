class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len( temperatures )
        answer = [0] *  n
        index_stack = list()

        for i in range(n):
            while ( len(index_stack) != 0 ):
                if (temperatures[i] > temperatures[index_stack[-1]] ):
                    answer [index_stack[-1] ] = i - index_stack[-1]
                    index_stack.pop()
                else:
                    break
            index_stack.append( i )    

        return answer        