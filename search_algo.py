import heapq
from node import PuzzleNode
import distance as ds
import helper as help 


def search(initial_state, target_state, heuristic):
    root_node = PuzzleNode(puzzle_state=initial_state)
    frontier = [root_node]
    heapq.heapify(frontier)
    node_expanded = 0
    explored = []
    max_size_queue = 1
    print_val = True

    while frontier:
        max_size_queue = max(len(frontier), max_size_queue)
        current_node = heapq.heappop(frontier)

        if print_val:
            print(f"\nThe state with a cost of g(n) = {int(current_node.cost_from_start)} and heuristic value of h(n) =  {int(current_node.heuristic_cost)} is now being expanded.")
            current_node.print_puzzle_state()
            print("----------------------------------------------------------------")

        if help.isstatesequal(current_node.puzzle_state, target_state):
            return help.print_solution(current_node, node_expanded, max_size_queue)

        explored.append(current_node)

        expanded_states = get_expanded_states(current_node)

        for state in expanded_states:
            new_node = PuzzleNode(puzzle_state=state)

            if should_skip_node(frontier, explored, new_node):
                continue

            update_heuristic_cost(new_node, target_state, heuristic)
            add_new_node_to_frontier(current_node, new_node, frontier)

        node_expanded += 1

    print("No solution found")
    return -1


def get_expanded_states(node):
    return list(filter(lambda x: x, node.generate_child_states()))


def should_skip_node(frontier, explored, new_node):
    return new_node in frontier or new_node in explored


def update_heuristic_cost(node, target_state, heuristic):
    if heuristic == "A*_misplaced":
        node.heuristic_cost = ds.misplaced_tiles(node.puzzle_state, target_state)
    elif heuristic == "A*_manhattan":
        node.heuristic_cost = ds.calculate_distance(node.puzzle_state, target_state)


def add_new_node_to_frontier(current_node, new_node, frontier):
    current_node.add_new_child(child_node=new_node)
    heapq.heappush(frontier, new_node)
    
