class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = list()
        for token in tokens:
            if ( token == '*' or token == '/' or token == '+' or token == '-'):
                operand2 = my_stack.pop()
                operand1 = my_stack.pop()

                if ( token == '*' ):
                    res = operand1 * operand2
                elif (token == '/' ):
                    res = int(operand1 / operand2)
                elif (token == '+' ):
                    res = operand1 + operand2
                else :
                    res = operand1 - operand2

                my_stack.append(res)
            else :
                my_stack.append( int ( token ))
        return my_stack[0]
            
        