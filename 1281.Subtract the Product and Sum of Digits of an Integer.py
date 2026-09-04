class Solution(object):
    def subtractProductAndSum(self, n):
        sums = 0
        prod = 1
        while n>0:
            sums = sums + n%10
            prod = prod * (n%10)
            n = n//10

        return prod-sums
        