class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums ,path:List[int], res:List[List[int]]):
            if len(path)>=2 and path not in res :
                res.append(path[:])
            if not nums:
                return
            for i in range(len(nums)  ):
                if (not path or path[-1] <= nums[i]):
                    path.append(nums[i])
                    backtrack( nums[i+1:],path, res  )
                    path.pop()
        answer = []
        backtrack(nums, [], answer)
        return answer