import heapq
import problem as p

def uniform_cost_search (p):
    start = p.initialState()
    priority_queue = [(0, start)] # (cost, node) tuple priority queue
    visited = set()
    parent = {start: None} # To keep track of the parent node for constructing the path
    cost_so_far = {start: 0} # To store the cumulative cost of reaching each node
    while priority_queue:
        #uniform cost search implementation
        current_cost, current_node = heapq.heappop(priority_queue)
        visited.add(current_node)
        if p.isGoal(current_node): #reconstruct the path from start to goal
            cost = cost_so_far[current_node]
            path = []
            while current_node:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1], cost #return the path in the correct order
        
        for neighbor, edge_cost in p.transition(current_node):
            if neighbor not in visited:
                new_cost = cost_so_far[current_node] + edge_cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    parent[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))
    return None