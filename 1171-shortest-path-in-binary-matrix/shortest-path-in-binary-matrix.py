import sys
from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        r=len(grid)
        c=len(grid[0])
        distance=[[sys.maxsize for _ in range(c)] for _ in range(r)]
        queue=deque()
        queue.append([1,0,0])
        while queue:
            dist,i,j=queue.popleft()
            if i== r-1 and j==c-1:
                        return dist
            for dx,dy in [[-1,0],[0,1],[1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]:
                new_i,new_j=i+dx,j+dy
                if new_i<0 or new_i==r or new_j<0 or new_j==c:
                    continue
                if grid[new_i][new_j]==1:
                    continue
                dist_trav=dist+1
                
                if dist_trav < distance[new_i][new_j]:
                    distance[new_i][new_j]=dist_trav
                    queue.append([dist_trav,new_i,new_j])
        return -1