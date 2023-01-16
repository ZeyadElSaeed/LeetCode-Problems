class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        answer = list()
        for i in range( 1 , len(nums) ):
            pre[i] = pre[i - 1] * nums[i -1]
        for i in range( len(nums) -2 ,  -1, -1):
            if ( i < 0):
                break
            post[i] = post[i+1] * nums[i+1]
        for i in range(len(nums)):
            answer.append( pre[i] * post[i] )
        return answer    
            
        