#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
		
		l=0
		r=len(s)-1
		
		while r>l:
		    if s[l] != s[r]:
		        return False
		    l=l+1
		    r=r-1
		return True