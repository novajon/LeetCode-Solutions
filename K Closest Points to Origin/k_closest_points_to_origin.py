# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        point_ind = []
        for ind, p in enumerate(points):
            point_ind.append(self.getEuclidean(p))
        
        K_el = []
        
        
        for k in range(K):
            low = point_ind[0]
            low_ind = 0
            for el_ind,el in enumerate(point_ind):
                if el < low:
                    low = point_ind[el_ind]
                    low_ind = el_ind
            K_el.append(points[low_ind])
            points.pop(low_ind)
            point_ind.pop(low_ind)
        return K_el
        
    def getEuclidean (self,p1):
        return p1[0]**2 + p1[1]**2
        
