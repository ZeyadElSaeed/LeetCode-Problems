class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        my_list = [0] * (n+1)
        for x,y in trust:
            my_list[x] -= 1
            my_list[y] += 1
        for i in range(1 , n+1):
            if my_list[i] == (n-1):
                return i
        return -1         