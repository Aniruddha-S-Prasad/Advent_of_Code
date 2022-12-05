from crate_mover import move_crates

with open('stack.txt', 'r') as init_stack_file:
    crate_arrangement = [
        (line.replace('[', ' ').replace(']', ' ').replace('   ', '.')) for line in init_stack_file
        ]
crate_arrangement.pop()

crate_arrangement = [
    [line[2 * ctr + 1] for line in crate_arrangement] for ctr in range(9)
    ]

for line in crate_arrangement:
    line.reverse()
    while line[-1] == '.' or line[-1] == ' ' or line[-1] == '\n':
        line.pop()
for line in crate_arrangement:
    print(line)

with open('input.txt', 'r') as instructions_file:
    instructions = [line.strip() for line in instructions_file]

instructions = [
    list(eval(line.replace('move ', '[').replace('from ', '').replace('to ', '').replace(' ', ',')+']')) for line in instructions
]

for line in instructions:
    x = [int(y) for y in line]
    # print(f'move {x[0]} from {x[1]} to {x[2]}')
    move_crates(x[0], crate_arrangement[x[1] - 1], crate_arrangement[x[2] - 1], crane_9001=True)

for line in crate_arrangement:
    print(line[-1], end='')
print()
