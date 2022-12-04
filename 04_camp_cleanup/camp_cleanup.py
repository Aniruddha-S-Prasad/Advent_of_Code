import numpy as np

with open('input.txt', 'r') as assignment_sheet:
    assignments = [pair.strip().split(',') for pair in assignment_sheet]

elf_1_assignments = np.array([[int(x) for x in pair[0].split('-')] for pair in assignments])
elf_2_assignments = np.array([[int(x) for x in pair[1].split('-')] for pair in assignments])

# Work for elf_1 contained in work for elf_2
one_in_two = (elf_1_assignments[:, 0] >= elf_2_assignments[:, 0]) & (elf_1_assignments[:, 1] <= elf_2_assignments[:, 1])
# Work for elf_2 contained in work for elf_1
two_in_one = (elf_2_assignments[:, 0] >= elf_1_assignments[:, 0]) & (elf_2_assignments[:, 1] <= elf_1_assignments[:, 1])

print((one_in_two | two_in_one).astype(int).sum())