class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = dict()
        for x in nums:
            if ( x in dictionary):
                return True
            dictionary[x] = True
            
        return False    
        