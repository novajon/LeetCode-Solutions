# https://leetcode.com/problems/unique-paths-iii/

import copy

class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        #at every position, we can walk up, right, left, down
        up = self.walk_path(copy.deepcopy(grid),"up")
        right = self.walk_path(copy.deepcopy(grid),"right")
        down = self.walk_path(copy.deepcopy(grid),"down")
        left = self.walk_path(copy.deepcopy(grid),"left")
        
        return up + right + down + left
    
    def walk_path(self,grid,direction):
        x,y = self.get_start_coordinates(grid)
        
        grid[x][y] = -1
        
        if direction == "up":
            x+=-1
        
        if direction == "right":
            y+=1
            
        if direction == "down":
            x+=1
        
        if direction == "left":
            y+=-1
        
        return self.checkPos(grid,x,y)
        
        #paths that we have already been to should be marked with -1
        
        #new starting point should be set to 1
    
    def get_start_coordinates(self,grid):
        for row_ind,row in enumerate(grid):
            for col_ind,col in enumerate(row):
                if col == 1:
                    return row_ind,col_ind
                
    def allPositionsCovered(self,grid):
        for row in grid:
            for col in row:
                if col in [-1,2]:
                    continue
                else:
                    return False
        return True

    def checkPos(self,grid,x,y):
        if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y] != -1:
            if grid[x][y] == 2:
                if self.allPositionsCovered(grid):
                    return 1
                else:
                    return 0
            else:
                grid[x][y] = 1
                return self.uniquePathsIII(grid)
        else:
            return 0
                    
