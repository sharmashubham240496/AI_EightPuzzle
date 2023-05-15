def isstatesequal(state1, state2):
    s1 = []
    for row in state1:
        for item in row:
            s1.append(item)

    s2 = []
    for row in state2:
        for item in row:
            s2.append(item)

    return s1 == s2

def getCoordinate(val, data):
    for i, row in enumerate(data):
        if val in row:
            return i, row.index(val)
    return None, None

def print_solution(current_node, expanded_nodes_count, max_queue_size):
    print("\nSolution found!")
    print("Printing All Nodes in the path:")
    trace = current_node.getAllStateNodes()
    print("----------------------")
    if trace:
        for t in trace:
            for row in t:
                print(row)

            print("----------------------")
    print("Depth is "+str(len(trace)-1))
    return expanded_nodes_count, max_queue_size