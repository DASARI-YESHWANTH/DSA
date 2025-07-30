from collections import deque
class Solution:
    def bfs(self,i,j,visited,grid):
        queue=deque()
        visited[i][j]=1
        queue.append((i,j))
        while queue:
            r,c=queue.popleft()
            for dx,dy in [(0,1),(-1,0),(0,-1),(1,0)]:
                new_i,new_j=r+dx,c+dy
                if new_i<0 or new_i==len(grid) or new_j<0 or new_j==len(grid[0]) :
                    continue
                if visited[new_i][new_j]==1:
                    continue
                if grid[new_i][new_j]=='0':
                    continue
                queue.append((new_i,new_j))
                visited[new_i][new_j]=1

    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        count=0
        visited=[[0 for _ in range(n)] for _  in range (m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and visited[i][j]==0:
                    count+=1
                    self.bfs(i,j,visited,grid)
        return count
        