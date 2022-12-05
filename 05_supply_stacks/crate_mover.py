def move_crates(num_crates: int, from_place: list, to_place: list, crane_9001: bool=False):
    if (crane_9001):
        crane_space = []
        while num_crates > 0:
            crane_space.append(from_place.pop())
            num_crates -=1
        crane_space.reverse()
        to_place.extend(crane_space)
    else:
        while num_crates > 0:
            to_place.append(from_place.pop())
            num_crates -= 1