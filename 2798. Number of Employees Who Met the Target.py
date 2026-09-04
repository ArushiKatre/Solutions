class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        counter = 0
        for i in hours:
            if i >= target:
                counter += 1
        return counter
        