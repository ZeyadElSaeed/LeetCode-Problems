class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = list()

        for c in s:
            if ( c == '(' or c == '{' or c == '['):
                stack.append(c)
            else:
                if ( len(stack) == 0):
                    return False
                temp = stack.pop()
                if ( (temp == '(' and c != ')') or (temp == '{' and c != '}') or (temp == '[' and c != ']')):
                    return False
        if ( len(stack) == 0):
            return True
        return False        