class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = [[s,p] for s,p in zip( position , speed)]
        stack = list()

        for p, s in sorted(posAndSpeed)[::-1]:
            stack.append( (target-p) / s)
            if ( len(stack) >= 2 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)