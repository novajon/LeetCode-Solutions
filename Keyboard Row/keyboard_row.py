# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        single_row_words = []
        
        for word in words:
            if word[0].lower() in row1:
                curr_row = row1
            elif word[0].lower() in row2:
                curr_row = row2
            else:
                curr_row = row3
            all_in_one = True
            for letter in word:
                if letter.lower() not in curr_row:
                    all_in_one = False
                    break
            if all_in_one:
                single_row_words.append(word)
                
        return single_row_words
