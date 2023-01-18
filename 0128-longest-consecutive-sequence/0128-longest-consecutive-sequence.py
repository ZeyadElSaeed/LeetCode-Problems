class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted ( nums )
        n = len( nums)
        if ( n == 0):
            return 0
        currentMax = 1
        globalMax = currentMax
        for i in range( 1 , n ):
            if ( nums[i] == ( nums[i - 1] + 1)):
                currentMax += 1
                globalMax = max( globalMax , currentMax)
            elif ( nums[i] == ( nums[i - 1]) ):
                continue
            else:
                currentMax = 1
        return globalMax        
        