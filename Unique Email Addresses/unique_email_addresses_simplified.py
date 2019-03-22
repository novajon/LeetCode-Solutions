# https://leetcode.com/problems/unique-email-addresses/

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = []
        
        for email in emails:
            local_name = email.split("@")[0]
            domain_name = email.split("@")[1]
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".","")
            unique_emails.append(local_name+"@"+domain_name)
        
        return len(set(unique_emails))
        
