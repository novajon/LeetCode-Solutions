# https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution:
    def projectionArea(self, grid: 'List[List[int]]') -> 'int':
        
        #birds perspective (projection on xy) is always equal to number of blocks
        xy = sum([1 for x in grid for y in x if y!=0])
        
        # xz perspective is max of each list element
        xz = sum(max(x) for x in grid)
        
        #yz perspective is max of each elements for each position in the list
        yz = sum([max([g[x] for g in grid]) for x in range(len(grid[0]))])
        
        return xy + xz + yz
        
