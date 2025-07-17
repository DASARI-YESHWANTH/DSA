class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        visited = [0] * len(adj)
        result = []

        def DFS(node, result, visited, adj):
            visited[node] = 1  # Mark node as visited
            result.append(node)
            for neighbor in adj[node]:
                if visited[neighbor] == 0:
                    DFS(neighbor, result, visited, adj)

        DFS(0, result, visited, adj)
        return result

            
            