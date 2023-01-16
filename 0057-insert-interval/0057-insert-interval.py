class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = list()
        if ( len(intervals) == 0 ):
            return [newInterval]
        for i in range(len(intervals)):
            interval = intervals[i]
            if ( interval[0] > newInterval[1] ):
                answer.append(newInterval)
                while(i < len(intervals)):
                    interval = intervals[i]
                    i = i+1
                    answer.append(interval)
                return answer
            elif (interval[1] < newInterval[0]):
                answer.append(interval)

            else :
                if (interval[0] < newInterval[0] ):
                    start = interval[0]
                else:
                    start = newInterval[0]

                if (interval[1] < newInterval[1] ):
                    end = newInterval[1]
                else:
                    end = interval[1]
                newInterval = [start , end]
        if ( newInterval in answer):
            return answer
        else:
            answer.append(newInterval)
            return answer


             