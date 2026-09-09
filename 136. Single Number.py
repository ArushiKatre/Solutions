def singleNumber(self, nums):
        unique_nums = set(nums)
        for i in unique_nums:
            if nums.count(i) == 1:
                return i