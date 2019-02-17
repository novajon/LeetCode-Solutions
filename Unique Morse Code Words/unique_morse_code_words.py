# https://leetcode.com/problems/unique-morse-code-words/

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        morse_alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_codes = self.create_codes(words,morse_alphabet)
        
        return len(morse_codes)

    def create_codes(self,words,alphabet):
        codes = []
        for word in words: 
            m_str = "".join([alphabet[ord(letter) - 97] for letter in word])
            if m_str not in codes:
                codes.append(m_str)
        
        print(codes)
        return codes
