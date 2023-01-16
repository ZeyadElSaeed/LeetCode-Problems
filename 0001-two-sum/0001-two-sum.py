class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = dict()
        for i in range( len(nums)):
            x = nums[i]
            if ( x in mydict):
                return [ mydict[x] , i ]
            else:
                mydict[ target - x ] = i        