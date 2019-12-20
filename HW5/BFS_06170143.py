# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        temp = []    
        cur = []
        if self.graph[s]:
            temp.append(s)
            while temp:
                add = temp.pop(0)
                cur.append(add)
                if self.find(add):
                    i = self.find(add)
                    for point in i:
                        if point in temp or point in cur:
                            pass
                        else:
                            temp.append(point)
                else:
                    pass
            print(cur)
            return cur
        else:
            return None
    def find(self, num):
            return self.graph[num]
    def DFS(self, s):

