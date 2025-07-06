class Solution:
    def checkKthBit(self, n, k):
        if (n>>k) & 1 == 0:
            return False
        return True
        