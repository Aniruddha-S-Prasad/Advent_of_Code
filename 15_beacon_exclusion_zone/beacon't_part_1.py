import numpy as np
from dataclasses import dataclass
from time import time

def manhattan_distance(loc_a: tuple[int, int], loc_b: tuple[int, int]) -> int:
    dist_x = abs(loc_b[0] - loc_a[0])
    dist_y = abs(loc_b[1] - loc_a[1])
    return dist_x + dist_y


@dataclass
class SensorBeaconPair:
    sensor_loc: tuple[int, int]
    beacon_loc: tuple[int, int]
    distance: int = 0
    
    def __post_init__(self) -> None:
        self.distance = manhattan_distance(self.sensor_loc, self.beacon_loc)

    def __str__(self) -> str:
        sensor_str = "Sensor Location: " + str(self.sensor_loc)
        beacon_str = "Beacon Location: " + str(self.beacon_loc)
        distance_str = "Manhattan Distance: " + str(self.distance)
        return sensor_str + ' ' + beacon_str + ' ' + distance_str


def parse_location(loc_str: str) -> tuple[int, int]:
    location = tuple(int(substring.split('=')[1]) for substring in loc_str.split(', '))
    return location


def main(loc_data: list[str], y_check: int):
    sb_pairs = [SensorBeaconPair(*list(map(parse_location, line.split(':')))) for line in loc_data]
    occupied_locs = set([x.sensor_loc for x in sb_pairs] + [x.beacon_loc for x in sb_pairs])

    x_min = min([pair.sensor_loc[0] - pair.distance for pair in sb_pairs])
    x_max = max([pair.sensor_loc[0] + pair.distance for pair in sb_pairs])
    x_row = np.zeros(x_max-x_min, dtype=np.int32)

    loop_start = time()
    for sensor in sb_pairs:
        y_dist = abs(sensor.sensor_loc[1] - y_check)
        if y_dist < sensor.distance:
            available_x = sensor.distance - y_dist
            left_lim = sensor.sensor_loc[0] - available_x - x_min
            right_lim = sensor.sensor_loc[0] + available_x - x_min
            x_row[left_lim:right_lim+1] = 1

    for location in occupied_locs:
        if (location[1] == y_check):
            x_row[location[0]-x_min] = 0
    
    num_covered_locs = np.sum(x_row)
    loop_end = time()
    print(f'Covered locations in row {y_check} is: {num_covered_locs}')
    print('Time in loop:')
    print(f'------ {loop_end-loop_start} seconds ------')

if __name__ == "__main__":
    demo = False
    if demo:
        input_filename = "demo.txt"
        y_check = 10
    else:
        input_filename = "input.txt"
        y_check = 2_000_000
    
    with open(input_filename, 'r') as input_file:
        input_data = [line.strip() for line in input_file]
   
    main(input_data, y_check)