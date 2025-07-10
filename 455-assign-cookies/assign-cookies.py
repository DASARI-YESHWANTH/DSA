class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        n=len(g)
        r=l=0
        k=len(s)
        count=0
        while r<k and l<n:
            if g[l]<=s[r]:
                count+=1
                l+=1
            r+=1
        return count
        