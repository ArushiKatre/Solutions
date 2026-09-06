def moveZeroes(nums):
        nums2 = []
        counter = 0
        for i in nums:
            if i != 0:
                nums2.append(i)
            else:
                counter += 1
        for i in range(counter):
            nums2.append(0)
        return nums2

print(moveZeroes([0,1,0,3,12]))