# https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        #define list to save unique special-equivalent strings
        individual_signature = []
        
        # for every string in input
        for a in A:
            #test if it is already contained in individuals list (or any of its equivalents)
            if self.isInIndividualList(a,individual_signature):
                individual_signature.append(a)
        return len(individual_signature)
        
    def isInIndividualList(self,a,individual_signature):
        if len(individual_signature)==0:
            return True
        sig_found = False
        for sig in individual_signature:
            for ind_s,s in enumerate(str(a)):
                if sig.count(s) != a.count(s):
                    sig_found = True
                    break
                elif s not in sig[ind_s%2::2]:
                    print("entered")
                    sig_found = True
                    break
                else:
                    sig_found = False
            if sig_found==False:
                return False
        
        return sig_found
        
