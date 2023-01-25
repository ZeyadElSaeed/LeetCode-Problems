class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        start = 0
        end = len(height) - 1

        while start < end :
            maximum = max( maximum , min(height[start] , height[end]) * ( end - start ))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maximum        