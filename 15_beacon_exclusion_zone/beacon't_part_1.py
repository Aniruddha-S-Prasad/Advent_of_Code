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


def coverage_union(coverage_desc: list[list[int]], addn_coverage: list[int]) -> None:
    item_added = False
    if len(coverage_desc) != 0:
        for coverage_item in coverage_desc:
            if (coverage_item[0] <= addn_coverage[0] <= coverage_item[1]) or (coverage_item[0] <= addn_coverage[1] <= coverage_item[1]):
                coverage_item[0] = min([coverage_item[0], addn_coverage[0]])
                coverage_item[1] = max([coverage_item[1], addn_coverage[1]])
                item_added = True
                break
        if not item_added:
            coverage_desc.append(addn_coverage)
    else:
        coverage_desc.append(addn_coverage)


def resolve_coverage(coverage_desc: list[int]) -> list[int]:
    to_be_deleted = []
    for i in range(len(coverage_desc)):
        for j in range(i+1, len(coverage_desc)):
            if (coverage_desc[j][0] <= coverage_desc[i][0] <= coverage_desc[j][1]) or (coverage_desc[j][0] <= coverage_desc[i][1] <= coverage_desc[j][1]):
                    coverage_desc[j][0] = min([coverage_desc[i][0], coverage_desc[j][0]])
                    coverage_desc[j][1] = max([coverage_desc[i][1], coverage_desc[j][1]])
                    to_be_deleted.append(i)
                    break
    for index in sorted(to_be_deleted, reverse=True):
        del coverage_desc[index]
    pass


def main(loc_data: list[str], y_check: int):
    sb_pairs = [SensorBeaconPair(*list(map(parse_location, line.split(':')))) for line in loc_data]
    occupied_locs = set([x.sensor_loc for x in sb_pairs] + [x.beacon_loc for x in sb_pairs])

    x_min = min([pair.sensor_loc[0] - pair.distance for pair in sb_pairs])
    x_max = max([pair.sensor_loc[0] + pair.distance for pair in sb_pairs])
    coverage = []

    loop_start = time()
    for sensor in sb_pairs:
        y_dist = abs(sensor.sensor_loc[1] - y_check)
        if y_dist < sensor.distance:
            available_x = sensor.distance - y_dist
            left_lim = sensor.sensor_loc[0] - available_x
            right_lim = sensor.sensor_loc[0] + available_x
            coverage_union(coverage, [left_lim, right_lim])
    resolve_coverage(coverage)

    num_devices_in_row = 0
    for location in occupied_locs:
        if location[1] == y_check:
            num_devices_in_row +=1
    
    num_covered_locs = sum([coverage_item[1] + 1 - coverage_item[0] for coverage_item in coverage]) - num_devices_in_row
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