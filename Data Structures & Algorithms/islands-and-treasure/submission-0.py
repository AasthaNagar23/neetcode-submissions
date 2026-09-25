from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        columns=len(grid[0])
        queue=deque()
        for r in range(rows):
            for c in range(columns):
                if grid[r][c]==0:
                    queue.append((r,c))
        distance=0

        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                directions=[(-1,0),(1,0),(0,1),(0,-1)]
                for dr, dc in directions:
                    nr=dr+r
                    nc=dc+c
                    if nr<0 or nr>=rows or nc<0 or nc>=columns:
                        continue
                    if grid[nr][nc]==2147483647:
                        grid[nr][nc]=distance+1
                        queue.append((nr,nc))
            distance+=1