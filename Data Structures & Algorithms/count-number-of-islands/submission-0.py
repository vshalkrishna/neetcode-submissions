class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        Row, Col = len(grid), len(grid[0])
        def island_find(r, c):
            queue = deque([(r,c)])#(0,1)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < Row and 0 <= nc < Col and grid[nr][nc] == '1':
                        grid[nr][nc] = '2'
                        queue.append((nr, nc))
            

            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    island_find(i, j)
                    count += 1
        return count