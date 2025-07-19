from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        count=0
        total_ones=0
        visited=[[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    total_ones+=1
                if i==0 or i==m-1 or j==0 or j==n-1:
                    if grid[i][j]==1:
                        if visited[i][j]==0:
                            queue.append((i,j))
                            visited[i][j]=1
        while queue:
            (i,j)=queue.popleft()
            count+=1
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_i,new_j=i+dx,j+dy
                if new_i<0 or new_i==m or new_j<0 or new_j==n:
                    continue
                if visited[new_i][new_j]==1:
                    continue
                
                if grid[new_i][new_j]==1 :
                    queue.append((new_i,new_j))
                    visited[new_i][new_j]=1
        return total_ones-count