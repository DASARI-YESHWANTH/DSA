"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        hash_map={}
        
        for i in range (0,len(arr)):
            hash_map[arr[i]]=hash_map.get(arr[i],0)+1
        
        if x in hash_map:
            return hash_map[x]
        else:
            return 0