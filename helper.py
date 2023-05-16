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


def get_init_input(num_rows):
    print("Enter your puzzle " + " enter space between numbers.\n")
    mat = [get_row(i + 1) for i in range(num_rows)]
    if not getCoordinate(0, mat)[0]:
        print("Error found")
        return None
    return mat

def get_row(row_number):
    r = input("Enter Data for row number " + str(row_number) + ": ")
    return [int(x) for x in r.split()] 

def get_goal_state(num_rows):
    goal_state = [[(j + 1) + (num_rows * i) for j in range(num_rows)] for i in range(num_rows)]
    goal_state[num_rows - 1][num_rows - 1] = 0

    print("\n Do you want default final state? y or n")
    [print(i) for i in goal_state]  
    goal_mode = input() or "y"

    if goal_mode != "y":
        print("Enter custom final  state " + " enter space between numbers.\n")
        goal_state = [get_row(i + 1) for i in range(num_rows)]
        if not getCoordinate(0, goal_state)[0]:
            print("Error Found")
            return None
        
    return goal_state

def get_row(row_number):
    row = input("Enter row number " + str(row_number) + ": ")
    return [int(x) for x in row.split()] 
