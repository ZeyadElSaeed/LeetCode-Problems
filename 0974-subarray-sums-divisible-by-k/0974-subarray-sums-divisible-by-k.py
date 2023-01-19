class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        remain = 0
        prefix_dict = dict()
        prefix_dict[0] = 1
        for num in nums:
            remain = (remain+num) % k
            res += prefix_dict.get(remain , 0)
            prefix_dict[remain] = 1 + prefix_dict.get(remain , 0)
        return res         