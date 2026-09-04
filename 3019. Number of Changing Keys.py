class Solution(object):
    def countKeyChanges(self, s):
        counter = 0
        for i in range (len(s)-1):
            if s.lower()[i] == s.lower()[i+1]:
                pass
            else:
                counter += 1
        return counter
