def thirdMax(self, nums):
        list = sorted(set(nums))
        if len(list) >= 3:
            return list[-3] 
        else:
            return list[-1]
        