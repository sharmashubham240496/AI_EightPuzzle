from time import perf_counter
from constants import ALGORITHM
import search_algo as sa
import helper as hp

def display_algorithm_options():
    print("\n\nSelect one algorithm from below:")
    for key, value in ALGORITHM.items():
        print(f" {key}  {value[1]}")

def print_execution_time(start, stop):
    print(f"\nExecution Time "+str(1000 * (stop - start))+"ms")



def select_search_algorithm():
    display_algorithm_options()    
    while True:
        user_input = input("\nEnter your choice 1, 2 or 3: ")
        if user_input in ALGORITHM.keys():
            print(f"\nSelected {ALGORITHM[user_input][1]}\n")
            return ALGORITHM[user_input][0]
        print("Wrong choice, please select a number from 1 to 3.")

def get_user_input():
    print(" 1) Use Default value of 3*3 puzzle" + "\n"
            + " 2) Set Custom value for puzzle" + "\n")

    while True:
        input_val = input() or "1"
        if input_val == "1":
            return get_default_puzzle()
        elif input_val == "2":
            num_rows = get_puzzle_size()
            return get_custom_puzzle(num_rows)
        else:
            print("Please input 1, 2")

def get_default_puzzle():
    initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
    target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return initial_state, target_state

def get_puzzle_size():
    print("Enter the Size for the square puzzle:")
    while True:
        try:
            num_rows = int(input())
            if num_rows < 0:
                raise ValueError
            return num_rows
        except ValueError:
            print("Error: Please input a valid number")

def get_custom_puzzle(num_rows):
    initial_state = hp.get_init_input(num_rows)
    if initial_state is None:
        initial_state = get_default_puzzle()[0]

    target_state = hp.get_goal_state(num_rows)
    if target_state is None:
        target_state = get_default_puzzle()[1]

    return initial_state, target_state




initial_state, target_state = get_user_input()

# initial_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
# initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
# initial_state = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
# initial_state = [[1, 3, 6], [5, 0,2], [4, 7, 8] ]
# initial_state = [[1, 3, 6], [5, 0,7], [4, 8, 2] ]


# initial_state = [[1, 6, 7], [5, 0, 3], [4, 8, 2]]
# initial_state = [[7, 1, 2], [4, 8, 5], [6, 3, 0]]
# initial_state = [[0, 7, 2], [4, 6, 1], [3, 5, 8]]
# target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


selected_algorithm = select_search_algorithm()

start_time = perf_counter()
node_expanded, max_size_queue = sa.search(initial_state, target_state, selected_algorithm)
print(f"\nThe search algorithm evaluated {node_expanded} nodes before reaching a solution.") 
print(f"\nThe queue reached a maximum size of {max_size_queue} nodes during the search algorithm's execution.")
end_time = perf_counter()
print_execution_time(start_time, end_time)
