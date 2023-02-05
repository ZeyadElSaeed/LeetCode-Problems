class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(nums, start , end ):
            while start < end :
                temp_val= nums[start]
                nums[start] = nums[end]
                nums[end] = temp_val
                start += 1
                end -= 1        
        n = len(nums)
        k = k % n
        reverse(nums, 0 , n-1 )
        reverse(nums, 0 , k-1 )
        reverse(nums, k , n-1 )         