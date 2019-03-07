# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import Counter

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        combine = A + " " + B
        counts = Counter(combine.split(" "))
        indv_words = []
        for key, value in counts.items():
            if value==1:
                indv_words.append(key)
                
        return indv_words
        
    
    def uncommonFromSentencesIterative(self, A: str, B: str) -> List[str]:
        a_words = A.split(" ")
        b_words = B.split(" ")
        indv_words=[]
        for ind,word in enumerate(a_words):
            if word not in b_words and word not in a_words[:ind] + a_words[ind+1:]:
                indv_words.append(word)
        for ind,word in enumerate(b_words):
            if word not in a_words and word not in b_words[:ind] + b_words[ind+1:]:
                indv_words.append(word)
        return indv_words
        
