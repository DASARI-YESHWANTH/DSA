class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dict={}
        l=0
        r=0
        maxi=0

        n=len(fruits)
        while r<n:
            if len(dict)==0:
                dict[fruits[r]]=0
            if fruits[r] not in dict:
                dict[fruits[r]]=0
                while len(dict)>2:
                    dict[fruits[l]]-=1
                    if dict[fruits[l]] ==0:
                        del dict[fruits[l]]
                    l=l+1


            dict[fruits[r]]+=1  
            maxi=max(maxi,r-l+1)
            r=r+1
        return maxi

        