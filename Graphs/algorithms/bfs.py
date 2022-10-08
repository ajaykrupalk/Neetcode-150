#To implement bread first search algorithm

'''
The concept of Breadth First Search is to traverse the graph level by level.
First find the root node, then find the nodes that are connected to the root node.
Then find the nodes that are connected to the nodes that are connected to the root node and so on.
'''

import collections

#recursive implementaion of Breadth First Search
def bfs_recursive(graph, queue, visited):
    if not queue:
        return
    
    vertex = queue.popleft()

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)
    bfs_recursive(graph, queue, visited)
    return visited

    

#iterative implementation of BFS
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        #remove the first element from the queue
        vertex = queue.popleft()
        print(str(vertex)+" ", end='')

        #check the adjacent nodes of the vertex
        for neighbor in graph[vertex]:
            #if adjacent nodes have not been visited, add them to the queue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {0: [1, 2,3], 1: [0,2], 2: [0,1,4], 3: [0], 4:[2]}
print(bfs_recursive(graph, collections.deque([0]), [0]))