# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected,  
# undirected and weighted graph 

from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
        self.graph_k = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
        self.graph_k[u][v] = w
    def Dijkstra(self, s): 
        """
        :type s: int
        :rtype: dict
        """
        unvisit = [i for i in range(len(self.graph))]       
        path = {}
        for i in range(len(self.graph)):
            path[i] = None
        path[s] = 0
        while unvisit != []:
            temp = self.temp_dic(unvisit,path)
            cur = self.find_min(temp)
            unvisit.pop(unvisit.index(cur)) 
            for index,i in enumerate(self.graph[cur]):
                if i != 0:
                    if path[index] == None:

                        path[index] = path[cur] + i
                    else:
                 
                        if path[cur] + i < path[index]:
                            path[index] = path[cur] + i

                else:
                    continue

        return path
    def temp_dic(self,unvisit,path):
        temp = {}
        for j in unvisit:
            temp_add = {j:path[j]}
            temp.update(temp_add)
        return temp
    def find_min(self,path):

        smallest =  min(path[x] for x in path if path[x] is not None)
        for v in path:
            if path[v] == smallest:
                smallest_key = v
            else:
                continue

        return smallest_key 
    def Kruskal(self):
        """
        :rtype: dict
        """
        # 開始某次找罪小的權重然後要注意不能有cycle
        # 每個點都有3次機會
        # stop = [i for i in range(len(self.graph_k))]*3
        # stop.sort()

        # stop.pop(stop.index(2))

        stop = {}
        for i in range(len(self.graph_k)):
            stop[i] = 3

        final = {}
        unvisit = [i for i in range(len(self.graph_k))]       
        temp = {}
        #建立初始temp當作搜尋用
        for i in range(len(self.graph_k)):
            for index,j in enumerate(self.graph_k[i]):
                if j != 0:
                    temp[j] = [index,i]

        # for i in range(len(self.graph_k)):
        while unvisit != []:
            
            cur = self.find_min_edge(temp) 
            for i in range(len(self.graph_k)):
                if stop[i] <= 1:
                    break
                # else:
            new = {}
            final.update(cur)
            # print(cur)
            
            for  key,value in cur.items():
                key_del = key
                value_del = value
            temp.pop(key_del)
            stop[value_del[0]] = stop[value_del[0]]-1
            stop[value_del[1]] = stop[value_del[1]]-1
            # stop.pop(stop.pop(value_del[0]))
            # stop.pop(stop.index(value_del[1]))
            unvisit.pop(0)
            
        final_return = {}
        for key,value in final.items():
            new = {str(value[1])+'-'+str(value[0]):key}
            # final_return[value[0]] = key
            final_return.update(new)
        print(final_return)
        return final_return
    def find_min_edge(self,path):
        #開始找最小的
        # min_edge = min(path)
        # print(path)
        # a = {10: [1, 0], 6: [2, 0], 5: [3, 0], 15: [3, 1], 4: [3, 2]}
        temp = min(path)
        min_edge = {}
        min_edge[temp] = path[temp]

        return min_edge

g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
g.Kruskal()



# a = [1,2,3]
# b = [0,1,2]
# while a != []:
#     for i in b:
#         if i == 1:
#             break  
#         else:
#             print(i)
#     a.pop()    
#     print('hi')
