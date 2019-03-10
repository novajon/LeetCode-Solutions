# https://leetcode.com/problems/island-perimeter/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        #perimeter of each piece of island is number of surrounding 0s
        perimeter = 0
        
        # loop through grid to find all 1s
        for ind_row, row in enumerate(grid):
            for ind_col, col in enumerate(row):
                if col == 1:
                    perimeter += self.getPerimeter(grid,ind_row,ind_col)
        
        return perimeter
        
    def getPerimeter(self,grid,ind_row,ind_col):
        surroundings = 0
        if ind_row == 0:
            surroundings += 1
        elif grid[ind_row-1][ind_col]==0:
            surroundings += 1
        if ind_row == len(grid)-1:
            surroundings += 1
        elif grid[ind_row+1][ind_col]==0:
            surroundings += 1
        if ind_col == 0:
            surroundings += 1
        elif grid[ind_row][ind_col-1]==0:
            surroundings += 1
        if ind_col ==len(grid[0])-1:
            surroundings += 1
        elif grid[ind_row][ind_col+1]==0:
            surroundings += 1
        
        return surroundings
        
        
