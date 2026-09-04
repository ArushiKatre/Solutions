class Solution(object):
    def checkIfPangram(self, sentence):
        return all(char in sentence.lower() for char in "abcdefghijklmnopqrstuvwxyz")
        