def removeElement(nums, val):
        k = 0
        for i in nums:
            if i == val:
                k += 1
        return k

print(removeElement([3,2,2,3], 3))