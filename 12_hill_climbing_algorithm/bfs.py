import numpy as np
from collections import deque, namedtuple
import copy

Node = namedtuple('Node', ['location', 'parent'])


def main(topo: list[str]):
    for i in range(len(topo)):
        topo[i] = [ord(char) - 96 if char.islower() else (0 if char=='S' else 27) for char in topo[i]]
    topography = np.array(topo)

    start_loc = (int(np.where(topography == 0)[0]), int(np.where(topography == 0)[1]) )
    start_state = Node(location=start_loc, parent=None)
    goal = (int(np.where(topography == 27)[0]), int(np.where(topography == 27)[1]) )

    topography[start_state.location] = 1
    topography[goal] = 26
    print('--Part 1 Solution--')
    print(bfs_path_length(start_state, goal, topography))
    
    lengths = []
    for start_loc_y, start_loc_x in zip(np.where(topography == 1)[0], np.where(topography == 1)[1]):
        start_loc = (int(start_loc_y), int(start_loc_x))
        start_state = Node(location=start_loc, parent=None)
        bfs_length = bfs_path_length(start_state, goal, topography)
        if bfs_length is not None:
            lengths.append(bfs_length)
    print('--Part 2 Solution--')
    print(min(lengths))

def bfs_path_length(start_state: Node, goal: tuple, topography: np.ndarray)-> int:
    frontier = deque()
    explored = set()
    length = 0

    frontier.append(start_state)
    while len(frontier) != 0:
        current_node = frontier.popleft()
        for move in allowed_moves(current_node.location, topography):
            if move not in explored:
                if move == goal:
                    length = 1
                    while current_node.parent is not None:
                        length += 1
                        current_node = current_node.parent
                    return length
                else:
                    frontier.append(Node(location=move, parent=current_node))
                    explored.add(move)


def allowed_moves(location: tuple, topography: np.ndarray):
    moves = []
    for action in [(location[0], location[1]+1), (location[0], location[1]-1), (location[0]+1, location[1]), (location[0]-1, location[1])]:
        if check_index_in_bound(action, topography.shape) and (topography[action] - topography[location]) < 2:
            moves.append(action)
    return moves

def check_index_in_bound(location: tuple, array_shape: tuple) -> bool:
    row, col = location
    if row >= 0 and row < array_shape[0] and col >= 0 and col < array_shape[1]:
        return True
    else:
        return False 


if __name__ == "__main__":
    demo = False
    if demo:
        file_name = 'demo.txt'
    else: 
        file_name = 'input.txt'
    
    with open(file_name, 'r') as topo_file:
        topography = [line.strip() for line in topo_file]
    
    main(topography)
