class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def nextGreaterElement(array, x, index ):
            for i in range(index, len(array)):
                if x < array[i]:
                    return array[i]
            return -1
        
        answer = []
        for x in nums1:
            index = nums2.index(x)
            answer.append( nextGreaterElement(nums2, x, index ) )
        return answer
            
            
        