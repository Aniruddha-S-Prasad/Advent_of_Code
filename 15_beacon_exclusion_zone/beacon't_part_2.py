from operator import itemgetter, attrgetter
from time import time


class SensorBeaconPair:
    def __init__(self, sensor_loc: tuple[int, int], beacon_loc: tuple[int, int]) -> None:
        self.sensor_loc = sensor_loc
        self.beacon_loc = beacon_loc
        self.distance = self.manhattan_distance(self.sensor_loc, self.beacon_loc)

    def __str__(self) -> str:
        sensor_str = "Sensor Location: " + str(self.sensor_loc)
        beacon_str = "Beacon Location: " + str(self.beacon_loc)
        distance_str = "Manhattan Distance: " + str(self.distance)
        return sensor_str + ' ' + beacon_str + ' ' + distance_str
    
    def manhattan_distance(self, loc_a: tuple[int, int], loc_b: tuple[int, int]) -> int:
        dist_x = abs(loc_b[0] - loc_a[0])
        dist_y = abs(loc_b[1] - loc_a[1])
        return dist_x + dist_y


def parse_location(loc_str: str) -> tuple[int, int]:
    location = tuple(int(substring.split('=')[1]) for substring in loc_str.split(', '))
    return location


def resolve_coverage(coverage_desc: list[tuple[int, int]]) -> list[tuple[int, int]]:
    coverage_desc.sort(key=itemgetter(0, 1))
    coverage = []
    current_range = list(coverage_desc[0])
    for coverage_item in coverage_desc:
        if (current_range[0] <= coverage_item[0] <= current_range[1] + 1):
            current_range[1] = coverage_item[1] if coverage_item[1] > current_range[1] else current_range[1]
        else:
            coverage.append((current_range[0], current_range[1]))
            current_range = list(coverage_item)
    coverage.append((current_range[0], current_range[1]))
    return coverage


def main(loc_data: list[str], search_size: int):
    sb_pairs = [SensorBeaconPair(*list(map(parse_location, line.split(':')))) for line in loc_data]
    sb_pairs.sort(key=lambda sensor: sensor.sensor_loc[0])
    search_size_10_percent = search_size//10

    loop_start = time()
    for y_check in range(search_size):
        coverage = []
        initial = True
        for sensor in sb_pairs:
            y_dist = abs(sensor.sensor_loc[1] - y_check)
            if y_dist < sensor.distance:
                available_x = sensor.distance - y_dist
                left_lim = sensor.sensor_loc[0] - available_x
                right_lim = sensor.sensor_loc[0] + available_x
                coverage_item = (left_lim if left_lim > 0 else 0, right_lim if right_lim < search_size else search_size)

                if initial:
                    current_range = list(coverage_item)
                    initial = False
                elif (current_range[0] <= coverage_item[0] <= current_range[1] + 1):
                    current_range[1] = coverage_item[1] if coverage_item[1] > current_range[1] else current_range[1]
                else:
                    coverage.append((current_range[0], current_range[1]))
                    current_range = list(coverage_item)

        coverage.append((current_range[0], current_range[1]))
        coverage = resolve_coverage(coverage)

        if (y_check % search_size_10_percent == 0):
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