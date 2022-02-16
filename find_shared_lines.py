import argparse

def readlines_into_set(file):
    lines = set()

    with open(file) as f:
        lines.add = {line.rstrip() for line in f.readlines()}

    return lines


def exclude_shared_lines(files):
    lines = readlines_into_set(files.shift())

    for file in files:
        lines = lines - readlines_into_set(file)

    return lines


def shared_lines(files):
    lines = readlines_into_set(files.shift())

    for file in files:
        lines = lines & readlines_into_set(file)

    return lines


def join_lines(files):
    lines = readlines_into_set(files.shift())

    for file in files:
        lines = lines | readlines_into_set(file)

    return lines


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

args.execute(args.files)
