# https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        
        # sort array
        deck.sort()
        
        return self.arrangeDeck(deck,True)
    
    def arrangeDeck(self,deck,start_first):
        
        if len(deck)==1:
            return deck
        
        # create temp_array of size len(deck) with every second entry being None
        new_deck = [0]*len(deck)
        
        # if start_first == False:
        #    deck[0], deck[1] = deck[1], deck[0]
        
        fill = start_first
        add = 0
        if start_first:
            add = 1
        for ind in range(len(deck)):
            if fill:
                if not start_first:
                    new_deck[ind] = deck[0]
                    start_first = True
                else:    
                    new_deck[ind] = deck[int((ind+add)/2)]
                fill=False
            else:
                fill=True
            
        deck = deck[len(deck) - new_deck.count(0):len(deck)]
        
        print(deck)
        print(new_deck)
        next_step_deck = self.arrangeDeck(deck,start_first = fill)
        
        next_ind = 0
        for el_ind,el in enumerate(new_deck):
            if el == 0:
                new_deck[el_ind] = next_step_deck[next_ind]
                next_ind += 1
        
        return new_deck
            
        
        # save remaining cards to temp_left_cards
        
        # repeat above with deck = temp_left_cards and indicator of whether to start at 0 or 1
        
        # fill previous temp_array with new entries
