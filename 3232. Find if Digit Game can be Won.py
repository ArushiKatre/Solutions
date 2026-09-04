def canAliceWin(nums):
        singleDigit = 0
        doubleDigit = 0
        for i in nums:
            if len(str(i)) == 1:
                singleDigit += i
            else:
                doubleDigit += i
        if singleDigit != doubleDigit:
            return True
        else:
            return False

print(canAliceWin([5,5,5,25]))