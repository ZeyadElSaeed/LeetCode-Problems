class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = list()

        def twoSum( numbers , target):
            dictionary = dict()
            answer = []
            for x in numbers:
                if (x not in dictionary):
                    dictionary[target - x] = x
                else:
                    if ([dictionary[x] , x] not in answer):
                        answer.append([dictionary[x] , x])
            return answer

        x = nums[0]
        for i in range(n-2):
            if i > 0 and x == nums[i]:
                continue
            else:
                x = nums[i]

            two_sums = twoSum( nums[i+1:] , -1 * nums[i])
            if  two_sums:
                for sum in two_sums:
                    res.append([nums[i]] + sum)
        return res        