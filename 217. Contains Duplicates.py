def containsDuplicate(nums):
        output = []
        for i in nums:
            if nums.count(i)>1:
                output.append(True)
            else:
                output.append(False)
        if True in output:
             return True
        else:
             return False

print(containsDuplicate([2,14,18,22,22]))