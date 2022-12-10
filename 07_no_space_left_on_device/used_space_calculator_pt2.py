from Directory import RootDirectory, Directory

file_tree = RootDirectory()

all_dirs = []

with open('input.txt', 'r') as cmd_trace:
    for line in cmd_trace:
        current_string = line.strip().split(' ')

        if current_string[0] == '$' and current_string[1] == 'cd':
            if current_string[2] == '/':
                current_dir = file_tree
                all_dirs.append(current_dir)
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

all_dirs: list[Directory]
all_dirs.sort(key=lambda folder: folder.get_deep_file_size())

current_free_space = 70000000 - file_tree.get_deep_file_size()
space_required = 30000000 - current_free_space

for folder in all_dirs:
    if folder.get_deep_file_size() > space_required:
        print(folder.get_deep_file_size())
        break


