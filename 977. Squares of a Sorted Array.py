class Solution(object):
    def sortedSquares(self, nums):
        sq_list =[]
        for i in nums:
            sq_list.append(i*i)
        return sorted(sq_list)