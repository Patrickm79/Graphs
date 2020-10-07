import collections

def earliest_ancestor(ancestors, starting_node):
    
    parents_by_child = {}

    # Here we build a graph from input and get parent of each node

    # Then loop through ancestors and build a dict of parents to children
    for parent, child in ancestors:
        if child in parents_by_child:
            parents_by_child[child].append(parent)
        else:
            parents_by_child[child] = [parent]

    # Early exit if the starting node has no parents
    if starting_node not in parents_by_child:
        return -1

    path_queue = collections.deque() 

    #Save last path deququed
    last_path = [starting_node]

    path_queue.append(last_path)

    while len(path_queue) > 0:
        last_path = path_queue.popleft()
        oldest_ancestor = last_path[-1]

        # Find the longest path, rather than the shortest
        if oldest_ancestor in parents_by_child:
            # make sure lowest id goes in queue last
            parents_by_child[oldest_ancestor].sort(reverse=True) 
            for parent in parents_by_child[oldest_ancestor]:
                new_path = last_path.copy()
                new_path.append(parent)

                path_queue.append(new_path)
    # Using BFT and returning the last path in queue, this should be the longest path
    return last_path[-1]