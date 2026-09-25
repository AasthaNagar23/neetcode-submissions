class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        columns=len(heights[0])
        pacific=set()
        atlantic=set()
        def dfs(r,c,visited):
            if (r,c) in visited:
                return 
            visited.add((r,c))
            directions=[(-1,0),(1,0),(0,-1),(0,1)]
            for dr,dc  in directions:
                nr=r+dr
                nc=c+dc
                if nr<0 or nr>=rows or nc<0 or nc>=columns:
                    continue
                if heights[nr][nc]<heights[r][c]:
                    continue
                dfs(nr,nc,visited)
        for r in range(rows):
            dfs(r,0,pacific)
        for c in range(columns):
            dfs(0,c,pacific)
        for r in range(rows):
            dfs(r,columns-1,atlantic)
        for c in range(columns):
            dfs(rows-1,c,atlantic)
        result=[]
        for r in range(rows):
            for c in range(columns):
                if (r,c) in atlantic and (r,c) in pacific:
                    result.append((r,c))
        return result