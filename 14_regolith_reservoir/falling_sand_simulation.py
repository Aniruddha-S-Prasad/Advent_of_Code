import numpy as np

sand_origin = (0, 500)

def sand_sim(rock_map: np.ndarray, sand_loc: tuple[int]):
    # Sand falls vertically until it reaches an obstruction
    new_loc = None
    vertical_slice = rock_map[sand_loc[0]:, sand_loc[1]]
    ground = np.where(vertical_slice)[0][0] + sand_loc[0]

    if ground == (sand_loc[0] + 1):
        if not rock_map[sand_loc[0] + 1, sand_loc[1] - 1]:
            new_loc = (sand_loc[0] + 1, sand_loc[1] - 1)
        elif not rock_map[sand_loc[0] + 1, sand_loc[1] + 1]:
            new_loc = (sand_loc[0] + 1, sand_loc[1] + 1)
        else:
            rock_map[sand_loc] = True
            return
    else:
        new_loc = (ground - 1, sand_loc[1])
    if new_loc is not None:
        sand_sim(rock_map, new_loc)
    else:
        raise Exception("New Loc was not calculated before recursion")

def map_gen(rock_lines: tuple[list[int], list[int]]):
    col_min, col_max = np.min(rock_lines[1]), np.max(rock_lines[1])
    row_min, row_max = 0, np.max(rock_lines[0])
    # row_min is hardcoded to be zero as defined by the falling location of sand
    map = np.full((row_max - row_min + 1, col_max - col_min + 1), False)

    rock_line_rows = np.array(rock_lines[0])
    rock_line_cols = np.array(rock_lines[1])

    map[(rock_line_rows - row_min, rock_line_cols - col_min)] = True
    return map, (col_min, col_max), (row_min, row_max)

def print_map(rock_map: np.ndarray):
    for line in rock_map:
        for pt in line:
            print("#", end=" ") if pt else print(".", end=" ")
        print()
    return

def rock_line_parser(scan_line: str) -> list[tuple[int]]:
    # Will return all the coordinates which are occupied by a rock
    cordinates = scan_line.split(" -> ")
    rock_lines_rows = []
    rock_lines_cols = []
    for index in range(len(cordinates) - 1):

        start_pt = [int(x) for x in cordinates[index].split(",")]
        end_pt = [int(x) for x in cordinates[index + 1].split(",")]

        if start_pt[0] == end_pt[0]:
            # Vertical line
            range_pts = range(start_pt[1], end_pt[1] + 1) if start_pt[1] < end_pt[1] else range(end_pt[1], start_pt[1] + 1)
            [(rock_lines_rows.append(ctr), rock_lines_cols.append(start_pt[0])) for ctr in range_pts]
        else:
            # Horizontal line
            range_pts = range(start_pt[0], end_pt[0] + 1) if start_pt[0] < end_pt[0] else range(end_pt[0], start_pt[0] + 1)
            [(rock_lines_rows.append(start_pt[1]), rock_lines_cols.append(ctr)) for ctr in range_pts]

    return rock_lines_rows, rock_lines_cols

def main(scan_data: list[str], part_2: bool):
    rock_locs_rows = []
    rock_locs_cols = []

    for scan_line in scan_data:
        tmp = rock_line_parser(scan_line)
        rock_locs_rows.extend(tmp[0])
        rock_locs_cols.extend(tmp[1])
    
    rock_map, col_m, row_m = map_gen((rock_locs_rows, rock_locs_cols))

    if part_2:
        scan_data.append(f"{col_m[0] - 1000},{row_m[1] + 2} -> {col_m[1] + 1000},{row_m[1] + 2}")
        rock_locs_rows = []
        rock_locs_cols = []
        del rock_map, col_m, row_m

        for scan_line in scan_data:
            tmp = rock_line_parser(scan_line)
            rock_locs_rows.extend(tmp[0])
            rock_locs_cols.extend(tmp[1])
    
        rock_map, col_m, row_m = map_gen((rock_locs_rows, rock_locs_cols))

    ctr = 0
    while True:
        try:
            sand_sim(rock_map, (sand_origin[0] - row_m[0], sand_origin[1] - col_m[0]))
        except IndexError:
            break
        if rock_map[(sand_origin[0] - row_m[0], sand_origin[1] - col_m[0])]:
            ctr += 1
            break
        ctr += 1
    print(ctr)
    # print_map(rock_map)

if __name__ == "__main__":
    demo = False
    part_2 = True
    if demo:
        input_filename = "demo.txt"
    else:
        input_filename = "input.txt"
    
    with open(input_filename, 'r') as input_file:
        input_data = [line.strip() for line in input_file]
    
    main(input_data, part_2)