def dfs(graph):
    visited = set()
    res = []
    flag = 0
    while min_num(visited, graph) is not None:
        node = min_num(visited, graph)
        if flag == 0:
            flag = 1
        dfs_helper(visited, graph, res ,node)

    return res

def min_num(visited, graph):
    if len(visited) >= len(graph.keys()):
        return
    min_node = min([key for key in graph.keys() if key not in visited])
    return min_node

def dfs_helper(visited, graph, res, node):
    if node not in visited:
        visited.add(node)
        res.append(node)
        stack = graph[node]
        stack.reverse()
        for neighbour in stack:
            dfs_helper(visited, graph, res, neighbour)
            
            
import collections

def bfs(graph):
    visited = set()
    #flag = 0
    while min_num(visited, graph) is not None:
        node = min_num(visited, graph)
        #if flag == 0:
            #flag = 1
        visited.add(node)
        bfs_helper(visited, graph, node)

def bfs_helper(visited, graph, node):
    queue = collections.deque([node])
    while queue:
        cur_node = queue.popleft()
        print(cur_node)
        if cur_node not in graph.keys():
            visited.add(cur_node)
            continue
        for neighbor in graph[cur_node]:
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
