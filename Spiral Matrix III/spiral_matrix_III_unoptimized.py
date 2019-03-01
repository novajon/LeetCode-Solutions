# https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        # difficulty: determine jump in points at the borders
        
        # if border at east end of the field -> jump to next free row south of the current one
            #if there is no entry point south of the current row -> enter next free column from the south
                #if there is no entry point to columns from the south -> jump to next free row in the west
                    # if there is no entry point to row from the west -> jump to next entry point in the north
        
        #the following array stores the positions that are at x distance from the current node, e.g. in the first sublist, there will be the positions that are at 1 distance
        
        current_direction = [0,1]
        output = [[r0,c0]]
        writes = 1
        r = r0
        c = c0
        grid = [[0 for i in range(C)] for j in range(R)]
        grid[r0][c0] = 1
        
        while writes < C*R:
            if r + current_direction[0] < R and c + current_direction[1] < C and r + current_direction[0] >=0 and R and c + current_direction[1] >= 0:
                r += current_direction[0]
                c += current_direction[1]
                output.append([r,c])
                writes += 1
                grid[r][c] = writes
                current_direction_candidate = self.turn(current_direction[0],current_direction[1])
                if r + current_direction_candidate[0] < R and c + current_direction_candidate[1] < C and r+current_direction_candidate[0]>=0 and c + current_direction_candidate[1] >= 0:
                    if grid [r + current_direction_candidate[0]][c + current_direction_candidate[1]] == 0:
                        current_direction = current_direction_candidate
                else:
                    current_direction = self.turn(current_direction[0],current_direction[1])
                    entered = False
                    while not entered:
                        current_direction = self.turn(current_direction[0],current_direction[1])
                        if current_direction[0] == 1:
                            for temp in range (c+1,C):
                                if grid[0][temp] == 0:
                                    c = temp
                                    r = 0
                                    entered = True
                                    output.append([r,c])
                                    writes += 1
                                    grid[r][c] = writes
                                    break    
                        elif current_direction[0] == -1:
                            for temp in range (c-1,-1,-1):
                                if grid[R-1][temp] == 0:
                                    c = temp
                                    r = R-1
                                    entered = True
                                    output.append([r,c])
                                    writes += 1
                                    grid[r][c] = writes
                                    break    
                        elif current_direction[1] == 1:
                            for temp in range (r,-1,-1):
                                if grid[temp][0] == 0:
                                    r = temp
                                    c = 0
                                    entered = True
                                    output.append([r,c])
                                    writes += 1
                                    grid[r][c] = writes
                                    break    
                        else:
                            for temp in range (r+1,R):
                                if grid[temp][C-1] == 0:
                                    r = temp
                                    c = C-1
                                    entered = True
                                    output.append([r,c])
                                    writes += 1
                                    grid[r][c] = writes
                                    break

            else:
                current_direction = self.turn(current_direction[0],current_direction[1])
                entered = False
                while not entered:
                    current_direction = self.turn(current_direction[0],current_direction[1])
                    if current_direction[0] == 1:
                        for temp in range (c+1,C):
                            if grid[0][temp] == 0:
                                c = temp
                                r = 0
                                entered = True
                                output.append([r,c])
                                writes += 1
                                grid[r][c] = writes
                                break    
                    elif current_direction[0] == -1:
                        for temp in range (c-1,-1,-1):
                            if grid[R-1][temp] == 0:
                                c = temp
                                r = R-1
                                entered = True
                                output.append([r,c])
                                writes += 1
                                grid[r][c] = writes
                                break    
                    elif current_direction[1] == 1:
                        for temp in range (r,-1,-1):
                            if grid[temp][0] == 0:
                                r = temp
                                c = 0
                                entered = True
                                output.append([r,c])
                                writes += 1
                                grid[r][c] = writes
                                break    
                    else:
                        for temp in range (r+1,R):
                            if grid[temp][C-1] == 0:
                                r = temp
                                c = C-1
                                entered = True
                                output.append([r,c])
                                writes += 1
                                grid[r][c] = writes
                                break                            
                    
        return output
    
    def turn (self,p0,p1):
        if p0 == 0 and p1 == 1:
            p0 = 1
            p1 = 0
        elif p0 == 0 and p1 == -1:
            p0 = -1
            p1 = 0
        elif p0 == 1 and p1 == 0:
            p0 = 0
            p1 = -1
        else:
            p0 = 0
            p1 = 1
        
        return [p0,p1]
        
    
    def get_distance(self,origin, point):
        return max(abs(origin[0]-point[0]),abs(origin[1]-point[1]))
