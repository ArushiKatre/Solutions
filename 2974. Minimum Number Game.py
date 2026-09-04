def numberGame(nums):
    nums.sort()
    finalList = []

    for i in range(0, len(nums), 2):
        finalList.append(nums[i + 1])  
        finalList.append(nums[i])      

    return finalList

