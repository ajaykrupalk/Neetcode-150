#To implement depth first search algorithm

'''
The concept of Depth First Search is to traverse the graph depth wise.
In DFS, we start from the root node and explore each branch completely before moving on to the next branch.
DFS is also known as pre-order traversal. 
'''

#Recursive implementation of DFS
def dfs_recursive(graph, root, visited=None):
    if visited is None:
        visited = set()

    visited.add(root)
    print(str(root)+" ", end='')

    for neighbor in graph[root]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    # return visited

#Iterative implementation of DFS
def dfs(graph, root):
    visited, stack = set(), [root]
    visited.add(root)

    while stack:
        #remove the last element from the stack
        vertex = stack.pop()
        print(str(vertex)+" ", end='')

        #check the adjacent nodes of the vertex
        for neighbor in graph[vertex]:
            #if adjacent nodes have not been visited, add them to the stack
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

graph = {0: [1, 2,3], 1: [0,2], 2: [0,1,4], 3: [0], 4:[2]}
dfs_recursive(graph, 0)