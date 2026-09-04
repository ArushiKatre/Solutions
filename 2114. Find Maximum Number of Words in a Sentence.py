class Solution(object):
    def mostWordsFound(self, sentences):
        spaceCount = []
        for i in sentences:
            spaceCount.append(i.count(" "))
        return max(spaceCount)+1