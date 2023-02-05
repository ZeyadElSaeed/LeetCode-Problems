class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        zero_ptr = 0
        for i in range(n):
            if (nums[i] != 0):
                nums[zero_ptr], nums[i] = nums[i], nums[zero_ptr]
                zero_ptr += 1
        