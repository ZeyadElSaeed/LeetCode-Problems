class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_perimeter = 0
        start = 0
        end = start + 3
        
        while end < len(nums)+1:
            if sum(nums[start:end-1]) > nums[end-1]:
                max_perimeter = max( max_perimeter, sum(nums[start:end]))
            
            start += 1
            end = start + 3
        return max_perimeter
        