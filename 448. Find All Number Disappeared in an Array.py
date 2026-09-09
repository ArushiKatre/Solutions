def findDisappearedNumbers(nums):
        output = []
        nums_set = set(nums)
        for i in range(1,len(nums)+1):
            if i not in nums_set:
                output.append(i)
        return output
        