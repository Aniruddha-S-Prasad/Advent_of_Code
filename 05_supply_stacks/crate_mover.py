def move_crates(num_crates: int, from_place: list, to_place: list):
    while num_crates > 0:
        to_place.append(from_place.pop())
        num_crates -= 1