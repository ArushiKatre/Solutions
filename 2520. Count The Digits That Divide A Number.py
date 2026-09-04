class Solution(object):
    def countDigits(self, num):
        counter = 0
        num_copy = num
        while num>0:
            digit = num%10
            if num_copy % digit == 0:
                counter += 1
            num = num//10
        return counter