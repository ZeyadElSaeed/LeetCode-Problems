class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using Floyd's Algorithm
        slow = fast = 0
        
        #where two ptrs intersect in the cycle
        while True :
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        # indicate where cycle begins
        cur = 0
        while True:
            if cur == slow :
                return slow
            cur = nums[cur]
            slow = nums[slow] 
            
            
        