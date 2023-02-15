class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # get chars between "[" and "]"
                my_str = ''
                while stack[-1] != '[':
                    my_str = stack.pop() + my_str
                stack.pop()
                # get the number that is before "["
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                # multiply the string and push it inside the stack
                stack.append(my_str*k)
        
        return "".join(stack)
                    
            