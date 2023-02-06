class Solution:
    def longestPalindrome(self, s: str) -> int:
        dictionary = {}
        for letter in s :
            dictionary[letter]=dictionary.get(letter,0)+1
        max_odd = 0
        res = 0
        for key in dictionary:
            if dictionary[key]%2 == 0:
                res += dictionary[key]
            else:
                res += dictionary[key] - 1
                max_odd = 1
        return res + max_odd        