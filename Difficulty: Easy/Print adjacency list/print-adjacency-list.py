
from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        # code here
        A_list=[[] for _ in range(V+1)]
        
        for u,v in edges:
            A_list[u].append(v)
            A_list[v].append(u)
        return A_list
        