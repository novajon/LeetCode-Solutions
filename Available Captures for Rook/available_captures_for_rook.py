class Solution(object):
    
    def findRookPos(self,board):
        for row_ind,row in enumerate(board):
            for col_ind,col in enumerate(row):
                if col == "R":
                    return (row_ind,col_ind)
    
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        rook_pos = self.findRookPos(board)
        
        east = board[rook_pos[0]][rook_pos[1]+1:]
        west = board[rook_pos[0]][0:rook_pos[1]]
        west = west[::-1]
        north = []
        for r in board[:rook_pos[0]]:
            north.append(r[rook_pos[1]])
        north = north[::-1]
        south = []
        for r in board[rook_pos[0]+1:]:
            south.append(r[rook_pos[1]])
        
        print ([east,west,north,south])
        
        for direction in [east,west,north,south]:
            for el in direction:
                if el == "p":
                    count += 1
                    break
                if el == "B":
                    break
        
        return count

                
        
