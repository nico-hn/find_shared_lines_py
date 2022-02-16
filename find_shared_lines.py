import argparse

def readlines_into_set(file):
    lines = set()

    with open(file) as f:
        lines |= {line.rstrip() for line in f.readlines()}

    return lines

def repeat_on_files(files, action):
    lines = readlines_into_set(files.pop(0))

    for file in files:
        new_lines = readlines_into_set(file)
        lines = action(lines, new_lines)

    return lines


def exclude_shared_lines(files):
    action = lambda lines, new_lines: lines - new_lines
    return repeat_on_files(files, action)


def shared_lines(files):
    action = lambda lines, new_lines: lines & new_lines
    return repeat_on_files(files, action)


def join_lines(files):
    action = lambda lines, new_lines: lines | new_lines
    return repeat_on_files(files, action)


tool_description = 'Find lines that are commonly included in given files.'

parser = argparse.ArgumentParser(description=tool_description)

parser.add_argument('files', metavar='FILE', type=str, nargs='+',
                    help='File that contains lines')

parser.add_argument('-e', '--exclude-shared-lines',
                    help='Exclude lines commonly included in given files',
                    action='store_const', const=exclude_shared_lines,
                    default=shared_lines, dest='execute')

parser.add_argument('-s', '--shared-lines ',
                    help='Collect lines shared in given files',
                    action='store_const', const=shared_lines,
                    default=shared_lines, dest='execute')

parser.add_argument('-j', '--join-lines',
                    help='Collect all lines in given files',
                    action='store_const', const=join_lines,
                    default=shared_lines, dest='execute')

args = parser.parse_args()

lines = args.execute(args.files)

sorted_lines = list(lines)
sorted_lines.sort()

for line in sorted_lines:
    print(line)
