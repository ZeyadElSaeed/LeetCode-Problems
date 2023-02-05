class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start_ptr = 0
        end_ptr = len(nums) - 1
        n = len(nums)
        res = [0] * n

        while start_ptr <= end_ptr:
            n -= 1
            if abs(nums[start_ptr]) < abs(nums[end_ptr]):
                res[n] = nums[end_ptr]** 2
                end_ptr -= 1
            else:
                res[n] = nums[start_ptr]** 2
                start_ptr += 1
        return res        