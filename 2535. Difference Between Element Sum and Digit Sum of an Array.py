class Solution(object):
    def differenceOfSum(self, nums):
        sum_elements = 0
        sum_digits = 0
        for i in nums: 
            sum_elements += i
            while i > 0:
                sum_digits += i%10
                i = i//10
        return abs(sum_elements - sum_digits)
        