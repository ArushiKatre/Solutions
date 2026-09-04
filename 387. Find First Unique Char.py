class Solution(object):
    def firstUniqChar(self, s):
        
        for i in range(len(s)):
            if s.find(s[i]) == s.rfind(s[i]):
                return i

        return -1