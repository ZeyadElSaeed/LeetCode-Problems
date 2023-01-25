class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1

        def notAlphanumeric(char):
            if char < 'a' or char > 'z':
                if char > '9' or char < '0':
                    return True
            return False

        while start < end:
            if notAlphanumeric(s[start]):
                start += 1
                continue
            if notAlphanumeric(s[end]):
                end -= 1
                continue

            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True        
        