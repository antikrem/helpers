# Detree folders

import sys
import os
from shutil import rmtree, move

working_directory = os.getcwd()

seperator = '_'

class ParsingError(Exception):
    def __str__(self):
        return 'Failed to parse correctly'
        
    def __repr__(self):
        return str(type(self))


def parse_and_apply_args() :
    args = sys.argv[1:]
    if len(args) > 0 :
        working_directory = args[0]


# If target is a file, returns target
# Otherwise calls find_all_files
def expand_token(target) :
    if os.path.isfile(target) :
        return target

    elif os.path.isdir(target) :
        return find_all_files(target)

    else :
        print(target)
        raise ParsingError


def find_all_files(folder) :
    files = os.listdir(folder)

    return [expand_token(os.path.join(folder, x)) for x in files]


# Changes absolute path to relative name
def path_to_name(path) :
    return path[len(working_directory) + 1:].replace('\\', seperator)

def recursivly_move(target) :
    if isinstance(target, str) :
        move(target, path_to_name(target))
    else :
        for i in target : recursivly_move(i)


def delete_old_folders(root) :
    for i in os.listdir(root) :
        target = os.path.join(root, i)
        if  os.path.isdir(target) :
            rmtree(target)


def main() :
    parse_and_apply_args()

    file_tree = find_all_files(working_directory)

    recursivly_move(file_tree)

    delete_old_folders(working_directory)

if __name__ == "__main__":
    main()