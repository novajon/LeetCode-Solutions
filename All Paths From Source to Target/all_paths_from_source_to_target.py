# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        #start at 0
        #for every index at position:
            #get path from index
            #until path = []
        return self.traverseGraph(graph,0)
        
    def traverseGraph(self,graph,ind):
        all_paths = []
        if not graph[ind]:
            all_paths.append([ind])
        for num in graph[ind]:
            paths = []
            traversed_paths = self.traverseGraph(graph,num)
            for trav_ind,trav_path in enumerate(traversed_paths):
                paths.append([ind])
                paths[trav_ind].extend(trav_path)
            all_paths.extend(paths)
        return all_paths
        
