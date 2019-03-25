# https://leetcode.com/problems/number-of-recent-calls/

from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.pingstory = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        while True:
            if len(list(self.pingstory))>0:
                el = self.pingstory.popleft()
                if el >= t-3000:
                    self.pingstory.appendleft(el)
                    break
            else:
                break
        self.pingstory.append(t)
        return len(list(self.pingstory))
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
