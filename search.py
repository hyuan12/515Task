#DFS
def dfs(graph):
    visited = set()
    while min_num(visited, graph) is not None:
        node = min_num(visited, graph)
        dfs_helper(visited, graph, node)

def dfs_helper(visited, graph, node):
    if node not in visited:
        visited.add(node)
        if node not in graph.keys():
            print(node)
            return
        stack = graph[node]
        stack.reverse()
        print(node)
        for neighbour in stack:
            dfs_helper(visited, graph, neighbour)
            
#find that smallest ndoe that hasn't been visited
def min_num(visited, graph):
    if len(visited) >= len(graph.keys()):
        return
    min_node = min([key for key in graph.keys() if key not in visited])
    return min_node
            
#BFS      
import collections

def bfs(graph):
    visited = set()
    while min_num(visited, graph) is not None:
        node = min_num(visited, graph)
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
