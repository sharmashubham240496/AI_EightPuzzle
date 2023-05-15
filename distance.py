import helper as help
from math import sqrt

def calculate_distance(state, goal, dist_type = 'manhattan'):
    all_dist = []
    for i, row in enumerate(state):
        for j, val in enumerate(row):
            if val == goal[i][j] or val == 0:
                continue
            i_of_goal_tile, j_of_goal_tile = help.getCoordinate(val, goal)
            if dist_type == 'euclidean':
                distance = sqrt((i - i_of_goal_tile)**2 + (j - j_of_goal_tile)**2)
            elif dist_type == 'manhattan':
                distance = abs(i - i_of_goal_tile) + abs(j - j_of_goal_tile)
            all_dist.append(distance)
    return sum(all_dist)

def manhattan_distance(state, goal):
    return calculate_distance(state, goal, 'manhattan')

def misplaced_tiles(state, goal):
    flat_state = []
    for sublist in state:
        for val in sublist:
            flat_state.append(val)

    flat_goal = []
    for sublist in goal:
        for val in sublist:
            flat_goal.append(val)

    return sum(s != g and s != 0 for s, g in zip(flat_state, flat_goal))
