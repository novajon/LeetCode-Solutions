# https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Alex can always win the game, simply by determining if the sum of the elements at the odd indexes is higher than the sum of the elements at the even indexes
        # He will then always choose the elements whose index is odd or even (whichever sum is higher)
        # For example, if Alex determines that the sum of odd indexes is higher, then he will choose the last element (odd index), Lee will have to choose an even index and Alex can continue with his strategy of always choosing the odd index
        # Note: This strategy might not give Alex the optimal score, but the question asks whether Alex can win the game. With this strategy, he will always win the game.        

	return True
