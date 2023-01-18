class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = list()
        res = list()

        def recursion( openNumber:int , closedNumber:int):
            if ( openNumber == closedNumber == n):
                return res.append( "".join(stack))

            if ( openNumber < n):
                stack.append("(")
                recursion( openNumber + 1 , closedNumber)
                stack.pop()

            if ( closedNumber < openNumber ):
                stack.append( ")" )
                recursion( openNumber, closedNumber + 1)
                stack.pop()

        recursion(0,0)
        return res         