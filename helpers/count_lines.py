# Count Lines

import sys
import os
from time import sleep

code_file_extensions = (
    '.h',
    '.hpp',
    '.c',
    '.cpp',
    '.py',
    '.cs',
    '.bat',
    '.js',
    '.jsx',
    '.ts',
    '.tsx',
    '.html',
    '.css',
    '.asm',
    '.lua',
    '.vert',
    '.frag'
)

class ParsingError(Exception) :
    def __str__(self):
        return 'Failed to parse correctly'
        
    def __repr__(self):
        return str(type(self))

def get_working_directory() -> str :
    args = sys.argv[1:]
    return args[0] if len(args) > 0 else os.getcwd()

def size(target: str) -> tuple[int, int] :
    if os.path.isfile(target) :
        return [1,  sum(1 for _ in open(target))] if target.endswith(code_file_extensions) else [0, 0]

    elif os.path.isdir(target) :
        l = [size(os.path.join(target, entry)) for entry in os.listdir(target)] + [[0, 0]]
        return [sum(x) for x in zip(*l)]

    else :
        raise ParsingError

def main() :
    working_directory = get_working_directory()

    file_count, line_count = size(working_directory)

    print('File Count   ', file_count)
    print('Line Count   ', line_count)

    sleep(5)

if __name__ == "__main__":
    main()