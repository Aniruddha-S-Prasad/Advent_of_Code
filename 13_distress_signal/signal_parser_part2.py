from functools import cmp_to_key

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


def main(signal_str: list[str]):
    signal = []
    for index, line in enumerate(signal_str):
        if index % 3 == 2:
            continue
        else:
            signal.append(eval(line))
    signal.append([[2]])
    signal.append([[6]])
    signal = sorted(signal, key=cmp_to_key(lambda a, b : -1 if check_order(a, b) else 1 if check_order(b, a) else 0))
    index_mul = 1
    for index, line in enumerate(signal):
        if line == [[2]] or line == [[6]]:
            index_mul *= index + 1
    print(f"Decoder key is {index_mul}")
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