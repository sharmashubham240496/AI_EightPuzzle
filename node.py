import copy
import helper as helper_module

class PuzzleNode:
    def __init__(self, parent_node=None, puzzle_state=0, cost_from_start=0, heuristic_cost=0):
        self.parent_node = parent_node
        self.puzzle_state = puzzle_state
        self.cost_from_start = cost_from_start
        self.heuristic_cost = heuristic_cost
        self.child_nodes = []

    def __eq__(self, other):
        return self.puzzle_state == other.puzzle_state

    def __lt__(self, other):
        return (self.cost_from_start + self.heuristic_cost) < (other.cost_from_start + other.heuristic_cost)

    def add_child(self, child_node, cost_to_expand=1):
        child_node.cost_from_start = self.cost_from_start + cost_to_expand
        child_node.parent_node = self
        self.child_nodes.append(child_node)

    def print_puzzle_state(self):
        for row in self.puzzle_state:
            print(row)