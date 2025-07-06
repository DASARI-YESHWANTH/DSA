#User function Template for python3
class Solution:
	def setBit(self, n):
		n= (n+1) | n
		return n