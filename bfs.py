#  Breadth First Search Algorithm

#  Accept the graph and its starting point
#  Initialize a set visited to keep track of visited nodes
#  Initialize a queue and add starting node to it
#  Run loop Until there are no nodes left in the queue
#      Remove first node from queue
#      Process the node if not visited
#      print node 
#      Add the node to the set visited (Mark the node as visited)
#      Add all unvisited neighbours of the node to the queue
#  The order of the nodes visited by algorithm has been printed

from collections import deque

def bfs(graph, start):
    # Initialize a set to keep track of visited nodes
    visited = set()
    # Initialize a queue and add the starting node to it
    queue = deque([start])
    
    # Continue until there are no nodes left in the queue
    while queue:
        # Remove the first node from the queue
        node = queue.popleft()
        
        # Process the node if it hasn't been visited
        if node not in visited:
            print(node, end=" ")  # Print the node
            visited.add(node)  # Mark the node as visited
            # Add all unvisited neighbors of the node to the queue
            queue.extend(graph[node])

