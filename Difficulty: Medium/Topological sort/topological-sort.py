class Solution:
    def dfs(self,node,stack,adj_lst,V,visited):
        visited[node]=1
        
        for anode in adj_lst[node]:
            if visited[anode]==0:
                self.dfs(anode,stack,adj_lst,V,visited)
        stack.append(node)
                
    
    def topoSort(self, V, edges):
        # Code here
        stack=[]
        adj_lst=[[] for _ in range(V)]
        for u,v in edges:
            adj_lst[u].append(v)
        visited=[0 for _ in range(V)]
        for i in range(V):
            if visited[i]==0:
                self.dfs(i,stack,adj_lst,V,visited)
        return stack[::-1]