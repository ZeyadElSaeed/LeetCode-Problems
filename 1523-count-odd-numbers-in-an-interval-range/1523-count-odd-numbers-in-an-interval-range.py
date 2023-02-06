class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low = low if low%2 else low+1
        answer = 0 if low > high else (high-low)//2 +1
        return answer
        