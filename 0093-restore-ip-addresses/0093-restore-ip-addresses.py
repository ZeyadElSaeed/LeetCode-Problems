class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        
        def backtrack( s, ip_chunck, ip, result ):
            if ( ip_chunck == 4 and (not s)):
                return result.append(ip[:-1])
            for i in range(1,4):
                if (i>len(s)) or (i>1 and s[0]=='0') or (i>2 and int(s[:i])> 255):
                    continue
                backtrack( s[i:], ip_chunck + 1, ip+s[0:i]+'.', answer)
                
        backtrack( s, 0, '', answer)
        return answer
    
        