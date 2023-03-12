class Solution(object):
    def addBinary(self, a, b):
        return bin(int(str(a), 2)+int(str(b), 2))[2:]
