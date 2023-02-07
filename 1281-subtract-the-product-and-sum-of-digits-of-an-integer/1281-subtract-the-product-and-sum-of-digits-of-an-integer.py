class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        my_sum = 0
        my_product = 1
        s = str(n)
        for x in s:
            x = int(x)
            my_sum += x
            my_product *= x
        return (my_product - my_sum)
            
        