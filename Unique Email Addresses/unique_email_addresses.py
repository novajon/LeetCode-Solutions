# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        # get unique domain names
        
        # get unique local name signatures --> expand local names to simplest form
        
        local_names = []
        domain_names = []
        unique_count = 0
        
        
        for email in emails:
            is_unique = True
            local_name,domain_name = email.split("@")
            
            local_name = local_name.split("+")[0]
            local_name = "".join(local_name.split("."))
            
            if local_name in local_names and domain_name in domain_names:
                is_unique = False
            
            if domain_name not in domain_names:
                domain_names.append(domain_name)
            if local_name not in local_names:
                local_names.append(local_name)
            
            if is_unique:
                unique_count += 1
        
        return unique_count

