from Directory import RootDirectory, Directory

file_tree = RootDirectory()

all_dirs = []

with open('input.txt', 'r') as cmd_trace:
    for line in cmd_trace:
        current_string = line.strip().split(' ')

        if current_string[0] == '$' and current_string[1] == 'cd':
            if current_string[2] == '/':
                current_dir = file_tree
            elif current_string[2] == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.contents[current_string[2]]

        elif current_string[0] == '$' and current_string[1] == 'ls':
            continue

        elif current_string[0] == 'dir':
            current_dir.add_directory(current_string[1])
            all_dirs.append(current_dir.contents[current_string[1]])
        
        else:
            current_dir.add_file(current_string[1], int(current_string[0]))

print(f'Root folder size: {file_tree.get_deep_file_size()}')

sum_of_small_folders = 0
all_dirs: list[Directory]
for folder in all_dirs:
    if folder.get_deep_file_size() < 100000:
        sum_of_small_folders += folder.get_deep_file_size()

print(f'Sum of all folders with size less than 100000 is {sum_of_small_folders}')
