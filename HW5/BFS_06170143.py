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
        """
        :type s: int
        :rtype: list
        """
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
        temp = []    
        cur = []
        if self.graph[s]:
            temp.append(s)
            while temp:
                add = temp.pop()
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
# g = Graph()
# g.addEdge(0,1)
# g.addEdge(0,2)
# g.addEdge(1,2)
# g.addEdge(2,0)
# g.addEdge(2,3)
# g.addEdge(3,3)

# g.DFS(2)

'''

[縱向優先搜尋 (depth-first search)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dfs.html)

[橫向優先搜尋 (breadth-first search)](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/bfs.html)

[老師moodle](https://docs.google.com/presentation/d/e/2PACX-1vTma_vOZyE70O23KWw4I4Y78aAaT5fJSTq7Mae912kCwka_u5ZMWPoo14D86-x-57kZPbb6hAGktSW4/pub?start=false&loop=false&delayms=3000&slide=id.g7aa022d8bc_2_5)

[老師的youtube影片](https://www.youtube.com/watch?v=DBnB60IOiw8&feature=youtu.be)
'''