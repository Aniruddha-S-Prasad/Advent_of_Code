def check_order(left_signal: list, right_signal: list) -> bool:

    try:
        for left_item, right_item in zip(left_signal, right_signal, strict=True):
            # Check if either of the items are lists
            l_list_check, r_list_check = isinstance(left_item, list), isinstance(right_item, list)
            if l_list_check or r_list_check:
                l_arg = left_item if l_list_check else [left_item]
                r_arg = right_item if r_list_check else [right_item]

                item_check = check_order(l_arg, r_arg)
                if item_check is None:
                    continue
                else:
                    return item_check
            else:
                if left_item < right_item:
                    return True
                elif left_item > right_item:
                    return False
                else:
                    continue
    except ValueError as zip_error:
        if "argument 2 is longer than argument 1" in str(zip_error):
            return True
        else:
            return False

    return None


def main(signal: list[str]):
    index_sum = 0
    for index, line in enumerate(signal):
        if index % 3 == 0:
            left_signal = eval(line)
        elif index % 3 == 1:
            right_signal = eval(line)
            right_order = check_order(left_signal, right_signal)

            if right_order is None:
                raise Exception(f"Could not evaluate the order of {int(index / 3) + 1}")
            elif right_order:
                index_sum += int(index / 3) + 1
            
        else:
            continue
    print(f"Sum of indices is {index_sum}")
    return


if __name__ == "__main__":
    demo = False
    if demo:
        input_filename = "demo.txt"
    else:
        input_filename = "input.txt"
    
    with open(input_filename, 'r') as input_file:
        input_data = [line.strip() for line in input_file]
    
    main(input_data)