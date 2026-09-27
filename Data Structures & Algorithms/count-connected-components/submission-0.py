class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited=set()
        component=0
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for i in range(n):
            if i not in visited:
                component+=1
                dfs(i)
        return component