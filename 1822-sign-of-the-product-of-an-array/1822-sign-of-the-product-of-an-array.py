class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(product):
            if product:
                return 1 if product>0 else -1
            return 0
        
        product = 1
        for x in nums:
            product *= x
        return 0 if not len(nums) else signFunc(product)
        