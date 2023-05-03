dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        
        visited2 = [[0 for _ in range(n)] for _ in range(m)]
        
        sub_island_cnt = 0
        
        # find all islands in grid2 and check it's all 1 in grid1
        
        for i in range(m):
            for j in range(n):
                is_sub_island = False
                if grid2[i][j] and not visited2[i][j]:
                    is_sub_island = self.checkSubIsland(i, j, grid1, grid2, visited2)

                if is_sub_island:           
                    sub_island_cnt += 1

        
        return sub_island_cnt
    
    def inRange(self, x, y, grid2):
        m = len(grid2)
        n = len(grid2[0])
        
        return x>=0 and x<m and y>=0 and y<n
                
        
    def checkSubIsland(self, x, y, grid1, grid2, visited2):
        is_land = False
        is_sub_island = True
        
        if grid1[x][y]:
            is_land = True
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if self.inRange(nx, ny, grid2) and grid2[nx][ny] and not visited2[nx][ny]:
                visited2[nx][ny] = 1
                is_sub_new_island = self.checkSubIsland(nx, ny, grid1, grid2, visited2)
                
                if not is_sub_new_island:
                    is_sub_island = False
        
        return is_land and is_sub_island
    
    