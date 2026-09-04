class Solution(object):
    def addDigits(self, num):
        sum = 0
        while num > 0:
            sum += num%10
            num = num//10
            

        if len(str(sum)) != 1:
            return self.addDigits(sum)        
        
        return sum
       
        