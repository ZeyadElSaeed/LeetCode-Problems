class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] < 'a' or s[start] > 'z':
                if s[start] > '9' or s[start] < '0':
                    start += 1
                    continue
            if s[end] < 'a' or s[end] > 'z':
                if s[end] > '9' or s[end] < '0':
                    end -= 1
                    continue

            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True        
        