class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split()
        answer = ''
        for word in words_list:
            answer += word[::-1]+' '
        return answer[:len(answer)-1]
            
            
        