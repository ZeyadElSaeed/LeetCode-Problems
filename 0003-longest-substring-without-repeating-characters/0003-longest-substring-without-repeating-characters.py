class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        max_str = 0
        counter = 0
        i = 0
        if not s :
            return max_str

        while i < len(s):
            letter = s[i]
            if letter in letters:
                max_str = max( max_str, counter)
                i = letters[letter]
                letters = {}
                counter = 0
            else:
                letters[letter] = i
                counter += 1
            i += 1
        return max( max_str, counter)        