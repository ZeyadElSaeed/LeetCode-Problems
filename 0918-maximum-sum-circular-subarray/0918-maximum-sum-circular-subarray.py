class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(num_list):
            Sum , maxSum = num_list[0], num_list[0]
            for m in num_list[1:]:
                Sum = max(m, Sum + m)
                maxSum = max(Sum, maxSum)
            return maxSum
        
        k = kadane(nums)
        
        cirSum = 0
        
        for idx in range(len(nums)):
            cirSum +=nums[idx]
            nums[idx] = -nums[idx]
            
        cirSum = cirSum + kadane(nums)
        
        if cirSum > k and cirSum != 0: 
            return cirSum 
        else: 
            return k
    
         