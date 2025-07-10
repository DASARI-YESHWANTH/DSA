class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n=len(s)
        # mcnt=1
        # p=''
        # if len(s)==0:
        #     return 0
        # for i in range(n):
        #     p=''
        #     p+=s[i]
        #     for j in range(i+1,n):
        #         if s[i] !=s[j] and s[j] not in p:
        #             p+=s[j]
        #             mcnt=max(mcnt,len(p))
        #         else:
        #             break

                
        # return mcnt
        left=0
        right=0
        dict={}
        n=len(s)
        maxi=0
        while right<n:
            if s[right] in dict:
                left=max(left,dict[s[right]]+1)

            maxi=max(maxi,right-left+1)
            dict[s[right]]=right
            right+=1
        return maxi