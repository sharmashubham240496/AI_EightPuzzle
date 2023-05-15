import copy
import helper as helper_module

class PuzzleNode:
    def __init__(self, parent_node=None, puzzle_state=0, cost_from_start=0, heuristic_cost=0):
        self.parent_node = parent_node
        self.puzzle_state = puzzle_state
        self.cost_from_start = cost_from_start
        self.heuristic_cost = heuristic_cost
        self.child_nodes = []
    """Condition check for two state"""
    def __eq__(self, other):
        return self.puzzle_state == other.puzzle_state
    """Conditions for priority Queue"""
    def __lt__(self, other):
        return (self.cost_from_start + self.heuristic_cost) < (other.cost_from_start + other.heuristic_cost)

    def add_new_child(self, child_node, cost_to_expand=1):
        child_node.cost_from_start = self.cost_from_start + cost_to_expand
        child_node.parent_node = self
        self.child_nodes.append(child_node)

    def generate_child_states(self):
        potential_states = []
        row_zero, col_zero = helper_module.getCoordinate(0, self.puzzle_state)
        size = len(self.puzzle_state)
        """All Possible movements"""
        movement_directions = [(row_zero-1, col_zero, 'up'), (row_zero+1, col_zero, 'down'), (row_zero, col_zero-1, 'left'),(row_zero, col_zero+1, 'right')]

        for new_row, new_col, _ in movement_directions:
            if 0 <= new_row < size and 0 <= new_col < size:
                # deepcopy clone for the current state to create the new state
                temp_state = copy.deepcopy(self.puzzle_state)
                """Swapping the 0 tile"""
                temp_state[row_zero][col_zero], temp_state[new_row][new_col] = temp_state[new_row][new_col], temp_state[row_zero][col_zero]
                """Appending the new state"""
                if not self.parent_node or not helper_module.isstatesequal(temp_state, self.parent_node.puzzle_state):
                    potential_states.append(temp_state)
        return potential_states

    def print_puzzle_state(self):
        for row in self.puzzle_state:
            print(row)

    def getAllStateNodes(self):
        node_path = []
        current_node = self
        while current_node:
            node_path.append(current_node.puzzle_state)
            current_node = current_node.parent_node
        return node_path[::-1]

    

    