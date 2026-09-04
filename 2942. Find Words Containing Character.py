class Solution(object):
    def findWordsContaining(self, words, x):
        base_list=[]
        j=0
        for i in words:
            j=j+1
            for char in i:
                if char == x:
                     base_list.append(j-1)
                     break
        return base_list