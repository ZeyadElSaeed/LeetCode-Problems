class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
                
        def fillStack(string):
            stack = list()
            for letter in string:
                if letter == '#' and len(stack) > 0:
                    stack.pop()
                elif letter != '#':
                    stack.append(letter)
            return stack

        return fillStack(s) == fillStack(t)
                    
            
        