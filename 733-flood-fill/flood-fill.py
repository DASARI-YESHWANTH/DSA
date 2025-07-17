class Solution:
   
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        visited=deepcopy(image)
        initial_color=image[sr][sc]
        def dfs(i,j):
            if i<0 or i==m or j<0 or j==n:
                return
            if visited[i][j]==color:
                return
            
            if visited[i][j] != initial_color:
                return
            visited[i][j]=color
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i-1,j)
            dfs(i,j+1)
        dfs(sr,sc)
        return visited
        