#!/usr/bin/python3
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start_vertex, target):
        discovered_lst = [False] * len(self.graph)
        queue = list()
        queue.append(start_vertex)
        discovered_lst[start_vertex] = True
        
        while queue:
            #FIFO
            current_vertex = queue.pop(0)
            print (current_vertex)
            if current_vertex == target:
                return current_vertex
            for adjacent_vertex in self.graph[start_vertex]:
#                if adjacent_vertex == target:
#                    return adjacent_vertex
#not neccessary
                if discovered_lst[adjacent_vertex] == False:
                    queue.append(adjacent_vertex)
                    discovered_lst[adjacent_vertex] = True
                else:
                    continue

        return None

