import itertools


filename = 'input.txt'

def get_directory(root, path):
    dir = root
    for component in path.split('/')[1:]:
        if component in dir:
            dir = dir[component]
        else:
            return None
    return dir


def get_parent(root, path):
    parent_path = '/'.join(path.split('/')[:-1])
    return get_directory(root, parent_path)


def add_file(root, path, size):
    get_parent(root, path)[path.split('/')[-1]] = size


def add_directory(root, path):
    get_parent(root, path)[path.split('/')[-1]] = {}


def exists(root, path):
    return get_directory(root, path) is not None


def total_size(root, path, max_size_to_count=100000):
    total = 0
    for name, item in get_directory(root, path).items():
        if type(item) != dict:
            item = int(item)
            total += item if item <= max_size_to_count else 0
        else:
            total += total_size(root, f"{path}/{name}", max_size_to_count)
            print(f"Total after {path}/{name}: {total}")
    print(f"{path} size: {total}")
    return total


with open(filename) as input_file:
    lines = input_file.readlines()
lines = [line.strip() for line in lines]

root = {}
current_path = ''
current_line_number = 0
while current_line_number < len(lines):
    segments = lines[current_line_number].split(' ')
    if segments[0] == '$':
        if segments[1] == 'cd':
            if segments[2] == '..':
                current_path = '/'.join(current_path.split('/')[:-1])
            else:
                current_path += '/' + segments[2]

        elif segments[1] == 'ls':
            current_line_number += 1
            while current_line_number < len(lines):
                if lines[current_line_number][0] in '0123456789':
                    size, name = lines[current_line_number].split(' ')
                    add_file(root, f"{current_path}/{name}", size)
                elif lines[current_line_number][0:3] == 'dir':
                    _, name = lines[current_line_number].split(' ')
                    add_directory(root, f"{current_path}/{name}")
                else:
                    break
                current_line_number += 1
            current_line_number -= 1

    else:
        print(f"Syntax error in line {current_line_number}: {lines[current_line_number]}")

    current_line_number += 1

print(total_size(root, ''))