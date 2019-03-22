# https://leetcode.com/problems/unique-email-addresses/submissions/

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        
        for email in emails:
            local_name = email.split("@")[0]
            domain_name = email.split("@")[1]
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".","")
            unique_emails.add(local_name+"@"+domain_name)
        
        return len(unique_emails)
        
