class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        def sum_odd(arr, index):
            res = 0
            for i in range(index+1, len(arr)+1,2):
                res += sum( arr[index:i])
            return res
        
        
        res = 0
        for i in range(len(arr)):
            res += sum_odd( arr, i)
        return res
        