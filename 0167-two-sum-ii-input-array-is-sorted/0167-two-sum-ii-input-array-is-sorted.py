class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1

        while start < end :
            sum = nums[start] + nums[end]

            if sum == target:
                return [start+1 , end+1]
            if sum < target:
                start += 1
            else:
                end -= 1
        return [-1,-1]        