from dataclasses import dataclass


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


def main(loc_data: list[str], y_check: int, part_2: bool):
    sb_pairs = [SensorBeaconPair(*list(map(parse_location, line.split(':')))) for line in loc_data]

    x_min = min([pair.sensor_loc[0] - pair.distance for pair in sb_pairs])
    x_max = max([pair.sensor_loc[0] + pair.distance for pair in sb_pairs])

    occupied_locs = set([x.sensor_loc for x in sb_pairs] + [x.beacon_loc for x in sb_pairs])

    covered_locs = 0
    lock_on = False
    captured_sensor = None
    for x in range(x_min, x_max + 1):
        if ((x, y_check) in occupied_locs):
            continue
        
        if lock_on and (captured_sensor is not None):
            if manhattan_distance((x, y_check), captured_sensor.sensor_loc) <= sensor.distance:
                covered_locs +=1
            else:
                lock_on = False
                for sensor in sb_pairs:
                    if manhattan_distance((x, y_check), sensor.sensor_loc) <= sensor.distance:
                        covered_locs += 1
                        captured_sensor = sensor
                        lock_on = True
                        break
        else:
            for sensor in sb_pairs:
                if manhattan_distance((x, y_check), sensor.sensor_loc) <= sensor.distance:
                    covered_locs += 1
                    captured_sensor = sensor
                    lock_on = True
                    break

    print(covered_locs)
    

if __name__ == "__main__":
    demo = False
    part_2 = False
    if demo:
        input_filename = "demo.txt"
        y_check = 10
    else:
        input_filename = "input.txt"
        y_check = 2000000
    
    with open(input_filename, 'r') as input_file:
        input_data = [line.strip() for line in input_file]
    
    main(input_data, y_check, part_2)