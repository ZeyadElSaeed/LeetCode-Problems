class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited_nums = set()
        while n not in visited_nums:
            visited_nums.add(n)
            cur_res = 0
            while n > 0:
                cur_res += (n%10)**2
                n = n//10
            n = cur_res
            if n == 1:
                return True
            
        return False
                        
            
            
                
                
            
            
        