#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 18:25:43 2023

@author: whale
"""

def dfs(graph):
    visited = set()
    nodes = [num for num in graph.keys() if len(graph[num]) != 0]
    node = min(nodes)
    #print(node)
    helper(visited, graph, node)
    print(visited)
    
def helper(visited, graph, node):
    if node not in visited:
       
        visited.add(node)
        if node not in graph.keys():
            return
        for neighbour in graph[node]:
            helper(visited, graph, neighbour)
            
#dfs({0: [1], 1: [0, 1, 2], 2: [0], 3: [0, 1, 2, 4], 4: [3]})

def bfs(graph):
    nodes = [num for num in graph.keys() if len(graph[num]) != 0]
    node = min(nodes)
    visited = []
    bfs_helper(visited, graph, node)
    
def bfs_helper(visited, graph, node):
  visited.append(node)
  queue = []
  queue.append(node)

  while queue:
    s = queue.pop(0) 

    if s not in graph.keys():
        continue
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

#bfs({1: [2,3], 3:[2, 4], 4: [3]})
