class Solution(object):
    def maximumWealth(self, accounts):
        sums = 0
        base_list = []
        for i in accounts:
            for j in i:
                sums +=j
            base_list.append(sums)
            sums = 0
        return max(base_list)
        