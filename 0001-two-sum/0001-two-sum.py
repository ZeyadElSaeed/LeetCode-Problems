class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain_dict = {}
        for index, x in enumerate(nums):
            if x not in remain_dict:
                remain_dict[target-x] = index
            else:
                return [ remain_dict[x], index ]
        