class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        i=start ^ goal
        count=0
        
        for j in range(32):
            if (i &(1<<j)) !=0:
                count+=1
        return count