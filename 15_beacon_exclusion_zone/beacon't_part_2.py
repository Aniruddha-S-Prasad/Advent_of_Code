
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


def resolve_coverage(coverage_desc: list[int]) -> list[int]:
    for _ in range(2):
        to_be_deleted = []
        for i in range(len(coverage_desc)):
            for j in range(i + 1, len(coverage_desc)):
                if (coverage_desc[j][0] <= coverage_desc[i][0] <= coverage_desc[j][1] + 1) or (coverage_desc[j][0] - 1 <= coverage_desc[i][1] <= coverage_desc[j][1]):
                        coverage_desc[j][0] = min([coverage_desc[i][0], coverage_desc[j][0]])
                        coverage_desc[j][1] = max([coverage_desc[i][1], coverage_desc[j][1]])
                        to_be_deleted.append(i)
                        break
        for index in sorted(to_be_deleted, reverse=True):
            del coverage_desc[index]
        coverage_desc.reverse()
    return


def main(loc_data: list[str], search_size: int):
    sb_pairs = [SensorBeaconPair(*list(map(parse_location, line.split(':')))) for line in loc_data]

    loop_start = time()
    for y_check in range(search_size):
        coverage = []

        for sensor in sb_pairs:
            y_dist = abs(sensor.sensor_loc[1] - y_check)
            if y_dist < sensor.distance:
                available_x = sensor.distance - y_dist
                left_lim = sensor.sensor_loc[0] - available_x
                right_lim = sensor.sensor_loc[0] + available_x
                coverage.append([left_lim if left_lim > 0 else 0, right_lim if right_lim < search_size else search_size])
        resolve_coverage(coverage)
        
        if (y_check % 400_000 == 0):
            print(f"Completion: {y_check*100/search_size}") 

        if (len(coverage) > 1):
            print(y_check, coverage)
            print((coverage[0][1] + 1)*4_000_000 + y_check)
            break

    loop_end = time()
    print('Time in loop:')
    print(f'------ {loop_end-loop_start} seconds ------')

if __name__ == "__main__":
    demo = False
    if demo:
        input_filename = "demo.txt"
        search_size = 20
    else:
        input_filename = "input.txt"
        search_size = 4_000_000
    
    with open(input_filename, 'r') as input_file:
        input_data = [line.strip() for line in input_file]
   
    main(input_data, search_size)