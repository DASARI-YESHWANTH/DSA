class Solution:
    def dfs(self, node, parent, adj, visited):
        visited[node] = 1
        for adjnode in adj[node]:
            if not visited[adjnode]:
                if self.dfs(adjnode, node, adj, visited):
                    return True
            elif adjnode != parent:
                return True  # Found a back edge (cycle)
        return False  # No cycle found from this path

    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]  # Use V instead of v
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * V
        for i in range(V):  # Must check all components
            if not visited[i]:
                if self.dfs(i, -1, adj, visited):
                    return True
        return False
