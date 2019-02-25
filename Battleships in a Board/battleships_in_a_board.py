# https://leetcode.com/problems/battleships-in-a-board/

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        # boat count init 0
        boat_count = 0
        
        # Introduce list to track positions of currently detected vertical boats
        vertical_boats = [False]*len(board[0])
        
        # loop through rows
        for row_ind, row in enumerate (board):
            # Introduce boolean to track if we are currently following a horizontal boat 
            # while looping through rows
            current_ship = False
            
            for col_ind, element in enumerate(row):
                if element == "X":
                    if col_ind + 1 < len(row) and row[col_ind+1] == "X":
                        current_ship = True
                    else:
                        current_ship = False
                    
                    if row_ind + 1 < len(board) and board[row_ind+1][col_ind] == "X":
                        vertical_boats[col_ind] = True
                    else:
                        vertical_boats[col_ind] = False
                    
                    if vertical_boats[col_ind] or current_ship:
                        continue
                    else:
                        boat_count += 1
                        
                    
            print (vertical_boats)
            
        return boat_count
                            
