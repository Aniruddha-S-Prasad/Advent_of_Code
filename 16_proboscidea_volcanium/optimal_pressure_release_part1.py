from collections import deque, namedtuple
from operator import attrgetter
from time import time


class Valve:
    def __init__(self, name: str, flow_rate: int, connection_strings: set[str]) -> None:
        self.name = name
        self.flow_rate = flow_rate
        self.connection_strings = connection_strings
        return
    
    def __str__(self) -> str:
        return self.name
    
    def establish_connections(self, valve_list: list['Valve']) -> None:
        self.connections = [valve for valve in valve_list if valve.name in self.connection_strings]
        return


Node = namedtuple('Node', ['valve', 'parent'])

def shortest_path(source: Valve, target: Valve):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    # Using a tuple for further optimizations
    start_state = Node(valve=source, parent=None)
    
    # Using a queue data structure ('deque') from collections. 
    # Its used here for fast append and fast pop
    frontier = deque()
    explored = set()
    path = []
    frontier.append(start_state)

    while len(frontier) != 0:
        current_node = frontier.popleft()
        for valve in current_node.valve.connections:
            if valve not in explored:
                if valve == target:
                    path.append(valve)
                    while current_node.parent is not None:
                        path.append(current_node.valve)
                        current_node = current_node.parent
                    path.reverse()
                    return path
                else:
                    frontier.append(Node(valve, current_node))
                    explored.add(valve)

def valve_data_parser(valve_data: str):
    flow_rate_data, tunnel_data = valve_data.split(';')

    valve = flow_rate_data.split(' ')[1]
    flow_rate = int(flow_rate_data.split('rate=')[1])

    tunnel_split = tunnel_data.split('valves ')
    if len(tunnel_split) == 1:
        tunnel_split = tunnel_data.split('valve ')
    tunnels = set(tunnel_split[1].split(', '))

    return Valve(name=valve, flow_rate=flow_rate, connection_strings=tunnels)


def benifit_calculator(minutes_left: int, start_valve: Valve, unexplored: set[Valve]):
    if len(unexplored) == 0:
        return 0
    else:
        benifits = []
        for destination_valve in unexplored:
            path = shortest_path(start_valve, destination_valve)
            cost = len(path) + 1
            if (minutes_left - cost) <= 0:
                benifit = 0
            else:
                benifit = (minutes_left - cost)*destination_valve.flow_rate + benifit_calculator(minutes_left - cost, destination_valve, unexplored - {destination_valve})
            benifits.append(benifit)
        return max(benifits)


def main(input_data: list[str]):
    start_time = time()
    valve_list = [valve_data_parser(valve_desc) for valve_desc in input_data]
    valve_list.sort(key=attrgetter('flow_rate'), reverse=True)
    for valve in valve_list:
        valve.establish_connections(valve_list)
    
    start_valve = next(filter(lambda valve: valve.name == 'AA', valve_list))
    unexplored = set(filter(lambda valve: (valve != start_valve) and (valve.flow_rate != 0), valve_list))
    minutes = 30
    max_benifit = benifit_calculator(minutes, start_valve, unexplored)
    end_time = time()
    print(f'Maximum pressure that can be released: {max_benifit}')
    print(f'------ {end_time-start_time} seconds ------')
    

if __name__ == "__main__":
    demo = False
    if demo:
        input_filename = "demo.txt"
    else:
        input_filename = "input.txt"
    
    with open(input_filename, 'r') as input_file:
        input_data_str = [line.strip() for line in input_file]
   
    main(input_data_str)