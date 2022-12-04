import numpy as np

def main():
    with open('input.txt', 'r') as calorie_list:
        total_calorie_list = []
        current_elf_cals = 0

        for entry in calorie_list:
            if entry == '\n':
                total_calorie_list.append(current_elf_cals)
                current_elf_cals = 0
                continue
            current_elf_cals += int(entry)
    
    total_calorie_list = np.array(total_calorie_list)
    print(np.sort(total_calorie_list)[-3:].sum())

    return

if __name__=='__main__':
    main()