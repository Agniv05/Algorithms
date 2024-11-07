#  Depth First Search Algorithm

#  Input the graph, the starting point and an empty set visited
#  Initialize the visited set
#  Mark starting node as visited and add it to visited set
#  print starting node
#  If neighbour of start is in graph 
#     And if that neighbour is not visited
#         Call dfs function with the inputs graph, neighbour (in place of starting point) and visited 
#  Hence all nodes are once the starting point and thus printed
#  So the order of visiting nodes by the algorithm is printed 



def dfs(graph, start, visited=None):
    # Initialize the visited set on the first call
    if visited is None:
        visited = set()
    
    # Mark the starting node as visited
    visited.add(start)
    print(start, end=" ")  # Print the node
    
    # Recursively visit all unvisited neighbors
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
